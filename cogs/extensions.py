from discord.ext import commands
import discord
from .utils import checks
import wget
import aiofiles
import aiohttp

class Cogs:
    """Manage cogs for Osmibot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @checks.is_owner()
    async def cog(self, ctx):
        """Cog management commands for Osmibot."""
        if ctx.invoked_subcommand is None:
            await self.bot.say('Use .help cog for command usage')
    
    @cog.command(pass_context=True)
    @checks.is_owner()
    async def load(self, ctx, cog: str = None):
        """Load a cog"""
        if cog == None:
            await self.bot.say('Please specify a cog to load.')
        else:
            await self.bot.say('Loading cog "' + cog + '."')
            try:
                self.bot.load_extension('cogs.' + cog.lower())
                await self.bot.say('Successfully loaded cog "' + cog + '."')
            except Exception as e:
                await self.bot.say('Error! Check the console for more details.')
                print('Failed to load extension {}\n{}: {}'.format(cog, type(e).__name__, e))

    @cog.command(pass_context=True)
    @checks.is_owner()
    async def unload(self, ctx, cog: str = None):
        """Unload a cog"""
        if cog == None:
            await self.bot.say('Please specify a cog to unload.')
        else:
            await self.bot.say('Unloading cog "' + cog + '."')
            try:
                self.bot.unload_extension('cogs.' + cog.lower())
                await self.bot.say('Successfully unloaded cog "' + cog + '."')
            except Exception as e:
                await self.bot.say('Error! Check the console for more details.')
                print('Failed to load extension {}\n{}: {}'.format(cog, type(e).__name__, e))

    @cog.command(pass_context=True)
    @checks.is_owner()
    async def reload(self, ctx, cog: str = None):
        """Unload and reload a cog"""
        if cog == None:
            await self.bot.say('Please specify a cog to reload.')
        else:
            await self.bot.say('Reloading cog "' + cog + '."')
            try:
                self.bot.unload_extension('cogs.' + cog.lower())
                self.bot.load_extension('cogs.' + cog.lower())
                await self.bot.say('Successfully reloaded cog "' + cog + '."')
            except Exception as e:
                await self.bot.say('Error! Check the console for more details.')
                print('Failed to load extension {}\n{}: {}'.format(cog, type(e).__name__, e))

def setup(bot):
    bot.add_cog(Cogs(bot))