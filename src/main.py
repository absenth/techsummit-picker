import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    last = getlast()

    @bot.command()
    async def pickspot(ctx):
        pick, website = pickspot()
        if pick == last:
            pick, website = pickspot()
        else:
            await ctx.send(f"Picked {pick} as our next spot.  LINK: {website}")
            setlast(pick)

    @bot.command()
    async def getpicks(ctx):
        picks = getpicks()
        await ctx.sent("These are the next five spots:")
        await ctx.sent(f"{picks}")

    bot.run(token)


def pickspot():
    locations = {
        "ABGB": "https://theabgb.com/",
        "SABG": "https://southaustinbeergarden.com/",
        "Little Woodrows": "https://littlewoodrows.com/locations/austin-southpark/",
        "Doc's": "https://www.eatdrinkdocs.com/",
        "Moontower": "https://moontowersaloon.com/",
        "The Little Darlin": "https://www.thelittledarlin.com/",
        "Pint House Pizza": "https://www.pinthouse.com/lamar",
        "The Far Out Lounge": "http://www.thefaroutaustin.com/",
    }

    pick, website = random.choice(list(locations.items()))
    return pick, website


if __name__ == "__main__":
    main()
