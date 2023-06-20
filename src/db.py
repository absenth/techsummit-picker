import os
import psycopg2
import sqlalchemy as db
from dotenv import load_dotenv


def generate_engine():
    load_dotenv()
    dbname = os.getenv('DBNAME')
    dbhost = os.getenv('DBHOST')
    dbuser = os.getenv('DBUSER')
    dbpass = os.getenv('DBPASS')
    dbport = os.getenv('DBPORT')
    engine = db.create_engine("postgresql://dbuser:dbpass@dbhost:dbport/dbname")
    return engine


def setupdb():
    engine = generate_engine()
    metadata = db.MetaData()
    spots_table = db.Table(
        "spots",
        metadata,
        db.Column("id", db.Integer(), primary_key=True),
        db.Column("name", db.String),
        db.Column("website", db.String),
        db.Column("google_maps_link", db.String),
    )
    picked_spots_table = db.MetaData(
        "picked_spots",
        metadata,
        db.Column("id", db.Integer(), primary_key=True),
        db.Column("spot_id", db.Integer(), db.ForeignKey("spots.id")),
        db.Column("spot_name", db.String(), db.ForeignKey("spots.name")),
        db.Column("picked_date", db.DateTime()),
    )

    metadata.create_all(engine)


def get_last_picked_spot():
    engine = generate_engine()
    metadata = db.MetaData()
    picked_spots_table = db.Table(
        "picked_spots", metadata, autoload=True, autoload_with=engine
    )
    query = (
        db.select([picked_spots_table])
        .order_by(picked_spots_table.columns.picked_date.desc())
        .limit(1)
    )
    connection = engine.connect()
    result = connection.execute(query).fetchone()
    connection.close()
    return result


def add_spot(name, website, google_maps_link):
    engine = generate_engine()
    metadata = db.MetaData()
    spots_table = db.Table('spots', metadata, autoload=True, autoload_with=engine)
    connection = engine.connect()
    query = spots_table.insert().values(name=name, website=website, google_maps_link=google_maps_link)
    connection.execute(query)
    connection.close()


def del_spot(spot_id):
    engine = generate_engine()
    metadata = db.MetaData()
    spots_table = db.Table('spots', metadata, autoload=True, autoload_with=engine)
    connection = engine.connect()
    query = spots_table.delete().where(spots_table.columns.id == spot_id)
    connection.execute(query)
    connection.close()


def get_last_five_picks():
    engine = generate_engine()
    metadata = db.MetaData()
    picked_spots_table = db.Table('picked_spots', metadata, autoload=True, autoload_with=engine)
    query = db.select([picked_spots_table]).order_by(picked_spots_table.columns.picked_date.desc()).limit(5)
    connection = engine.connect()
    result = connection.execute(query).fetchall()
    connection.close()
    return result