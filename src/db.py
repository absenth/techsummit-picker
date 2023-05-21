import os
import psycopg2
from dotenv import load_dotenv


def openconn():
    dbname = os.getenv('DBNAME')
    dbhost = os.getenv('DBHOST')
    dbuser = os.getenv('DBUSER')
    dbpass = os.getenv('DBPASS')
    dbport = os.getenv('DBPORT')

    conn = psycopg2.connect(database=dbname,
                            host=dbhost,
                            user=dbuser,
                            password=dbpass,
                            port=dbport)
    cursor = conn.cursor()
    return conn, cursor


def closeconn(conn, cursor):
    cursor.close()
    conn.close()


def setlast(name):
    conn, cur = openconn()
    cur.execute('do stuff')

    closeconn(conn, cur)
    return


def getlast():
    conn, cur = openconn()
    cur.execute('do stuff')

    closeconn(conn, cur)
    return name


def updatepicks(spot, date):
    conn, cur = openconn()
    cur.execute('do stuff')

    closeconn(conn, cur)
    return


def getpicks():
    conn, cur = openconn()
    cur.execute('do stuff')

    closeconn(conn, cur)
    return


def addspot(name, website, address):
    conn, cur = openconn()
    cur.execute('do stuff')

    closeconn(conn, cur)
    return



