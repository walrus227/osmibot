from discord.ext import commands
import discord
from .utils import checks
import sys

class Owner:
    """Commands to be used only by the bot owner."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def die(self):
        """Shut down the bot."""
        try:
            await self.bot.say(':wave:')
            await self.bot.logout()
            sys.exit()
        except Exception:
            await self.bot.say('Insufficient Permissions.')

    @commands.command()
    @checks.is_owner()
    async def username(self, name: str):
        """Change the bot's username."""
        try:
            await self.bot.edit_profile(username = name)
            await self.bot.say('Changed bot username to ' + name + '.')
        except Exception as e:
            await self.bot.say('Error! Check the console for more details.')
            print('Could not change name to {}\n{}: {}'.format(name, type(e).__name__, e))

def setup(bot):
    bot.add_cog(Owner(bot))