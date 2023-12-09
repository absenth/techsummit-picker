import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.command()
    async def pickspot(ctx):
        pick,website=spot()
        await ctx.send(f'Picked {pick} as our next spot.  LINK: {website}')

    bot.run(token)


def spot():
    return pickspot()


def pickspot():
    locations = {
            'ABGB': 'https://theabgb.com/',
            'SABG': 'https://southaustinbeergarden.com/',
            'Little Woodrows': 'https://littlewoodrows.com/locations/austin-southpark/',
            "Doc's": "https://www.eatdrinkdocs.com/",
            'Moontower': 'https://moontowersaloon.com/',
            'Last Stand Brewery': 'https://laststandbrewery.com',
            'The Little Darlin': 'https://www.thelittledarlin.com/',
            'Aviator Pizza & Drafthouse': 'https://aviatorpizza.com',
            'Fast Friends Brewery': 'https://fastfriendsbeer.com',
            'Nomadic Beerworks': 'https://www.nomadicbeerworks.com',
            'Progress Coffee & Beer': 'https://www.progresscoffeeroasting.com',
            'Emerald Tavern': 'https://www.emeraldtaverngames.com'
            }

    spot, website = random.choice(list(locations.items()))
    return spot, website


if __name__ == '__main__':
    main()
