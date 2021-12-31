from discord.commands import slash_command
from discord.ext import commands
import discord
from discord.ext.commands.cooldowns import BucketType

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Error(bot))