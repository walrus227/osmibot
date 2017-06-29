import sys
import discord
from discord.ext import commands
import asyncio
import aiohttp
import json
import os

#Thanks for trying Osmibot!
#The bot can be run by entering your bot's token, NOT Client ID, into the string at the bottom of the file..
os.system('cls')

bot = commands.Bot(command_prefix=['.', 'Osmibot, ', 'Osmi, '], description='Version 2.0 of the Best Discord Bot to ever exist')
client = discord.Client()

token = 'MjQ4NTU2OTU5NTIxODMyOTYy.DDVLlQ.z0CLKs6JT2Nc7wZOfkyntYcOli4'

@bot.event
async def on_ready():
    os.system('title Osmibot')
    print('Logged in as ' + bot.user.name + ' (ID: ' + bot.user.id + ') on ' + str(len(client.servers)) + ' servers.')
    await bot.change_presence(game=discord.Game(name="v2.0"))

@bot.command()
async def die():
    await bot.say(':wave:')
    await client.logout()
    sys.exit()

@bot.command()
async def ping():
    await bot.say('Pong!')

bot.run(token)
