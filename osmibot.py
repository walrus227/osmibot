import sys
import discord
from discord.ext import commands
import asyncio
import aiohttp
import json
import os

#Thanks for trying Osmibot!
os.system('cls')
dir_path = os.getcwd()
if not dir_path == 'master':
    os.chdir('master')

bot = commands.Bot(command_prefix=['.', 'Osmibot, ', 'Osmi, '], description='Version 2.0 of the Best Discord Bot to ever exist')
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
    await bot.change_presence(game=discord.Game(name="v2.0"))

@bot.command()
async def die():
    await bot.say(':wave:')
    await client.logout()
    sys.exit()

@bot.command()
async def ping():
    await bot.say('Pong!')

try:
    bot.run(token)
except Exception:
    print("Please configure config.json with your bot's token first!")
    input('Press enter to continue...')
    sys.exit()
