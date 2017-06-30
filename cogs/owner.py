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

def setup(bot):
    bot.add_cog(Owner(bot))