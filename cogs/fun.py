from discord.ext import commands
import discord

class Fun:
    """Fun commands to use with friends"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def whoami(self, ctx):
        """Returns the user who ran the command."""
        await self.bot.say("Why, you're " + ctx.message.author.mention + ', of course!')

def setup(bot):
    bot.add_cog(Fun(bot))