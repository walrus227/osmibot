from discord.ext import commands
import discord

class Meta:
    """Tools for managing the server and bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        """Test bot functionality"""
        await self.bot.say('Pong!')

def setup(bot):
    bot.add_cog(Meta(bot))