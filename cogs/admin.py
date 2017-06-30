from discord.ext import commands
import discord
import asyncio
from .utils import checks

class Admin:
    """Commands for moderating members"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(ban_members=True)
    async def bannu(self, ctx, user: discord.Member, days: str = None):
        """Gloriously bans a user and deletes X days worth of messages.
        
        Minimum days 0, maximum 7. Defaults to 0."""
        if user == ctx.message.author:
            await self.bot.say("I'm not going to do that. Self-harm is bad.")
        else:
            await self.bot.say('DING')
            await asyncio.sleep(1)
            await self.bot.say('DONG')
            await asyncio.sleep(1)
            try:
                await self.bot.ban(user, delete_message_days=days)
                await self.bot.say(user.mention + ' BANNU!')
            except Exception as e:
                print('Ban failed!')
                print(e)
                await self.bot.say('Error! Check the console for details.')

            

    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        """Kicks a user.
        
        Usage: .kick @Criminal"""
        if user == ctx.message.author:
            await self.bot.say("I'm not going to do that. Self-harm is bad.")
        else:
            try:
                await self.bot.kick(user)
                await self.bot.say('Kicked ' + user.mention + '.')
            except Exception as e:
                print('Kick failed!')
                print(e)
                await self.bot.say('Error! Check the console for details.')

def setup(bot):
    bot.add_cog(Admin(bot))