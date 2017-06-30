import sys
import discord
from cogs.utils import checks
from discord.ext import commands
import asyncio
import aiohttp
import json
import os
import platform

#Thanks for trying Osmibot!
useros = platform.system()

inital_extensions = [
    'cogs.meta',
    'cogs.fun',
    'cogs.admin',
    'cogs.extensions',
    'cogs.owner',
    'cogs.admin'
]

if useros == 'Windows':
    os.system('cls')
else:
    os.system('clear')

bot = commands.Bot(command_prefix=['.', 'Osmibot, ', 'Osmi, '], description='Omnifunction text bot for Discord', pm_help=True)
client = discord.Client()

try:
    with open('config.json') as config_data:
        config = json.load(config_data)
        token = config['token']
        clientid = config['client']
except Exception:
    #There's going to be an issue here! The user hasn't configured their token.
    #We don't want ugly error text in the interface, so we'll do nothing until we try to run the bot.
    pass

@bot.event
async def on_ready():
    os.system('title Osmibot')
    print('Logged in as ' + bot.user.name + ' (ID: ' + bot.user.id + '.)')
    await bot.change_presence(game=discord.Game(name=".help"))

for extension in inital_extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

try:
    bot.run(token)
except Exception:
    print("Please configure config.json with your bot's token first!")
    input('Press enter to continue...')
    sys.exit()
