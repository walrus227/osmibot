import discord
from discord.ext import commands
import asyncio

#Thanks for trying Osmibot!
#The bot can be run by entering your bot's token, NOT Client ID, into the string at the bottom of the file..

bot = commands.Bot(command_prefix=['.', 'Osmibot, ', 'Osmi, '], description='Version 2.0 of the Best Discord Bot to ever exist')
client = discord.Client()

token = 'MjQ4NTU2OTU5NTIxODMyOTYy.DDVLlQ.z0CLKs6JT2Nc7wZOfkyntYcOli4'

print('Logging in...')

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' (ID: ' + bot.user.id + ',) on ' + str(len(client.servers)) + ' servers.')
    await bot.change_presence(game=discord.Game(name="v2.0"))

#Token goes below.
bot.run(token)
