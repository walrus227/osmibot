import sys
import discord
from discord.ext import commands
import asyncio
import aiohttp
import json

#Thanks for trying Osmibot!
#The bot can be run by entering your bot's token, NOT Client ID, into the string at the bottom of the file..

bot = commands.Bot(command_prefix=['.', 'Osmibot, ', 'Osmi, '], description='Version 2.0 of the Best Discord Bot to ever exist')
client = discord.Client()

token = 'MjQ4NTU2OTU5NTIxODMyOTYy.DDVLlQ.z0CLKs6JT2Nc7wZOfkyntYcOli4'

@bot.event
async def on_ready():
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

@bot.group()
async def cog():
    await bot.say('Cog Management for Osmibot. Subcommands are: \n ```install - Install a cog for Osmibot \n remove - Remove an installed cog \n load - Load an installed cog \n unload - Unload an installed cog```')

@cog.command(pass_context=True)
async def install(ctx):
    await bot.say('Downloading cog...')
    async with aiohttp.get('{0}') as r:
        await bot.say('Downloaded ' + r)
        await bot.say('Loading cog...')
        await bot.say('jk just a test, sending file to commands channel')
        if r.status == 200:
            js = r.json()
            await client.send_message(295879222994665473, js['file'])

bot.run(token)
