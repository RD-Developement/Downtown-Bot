from discord.commands import slash_command  # Importing the decorator that makes slash commands.
from discord.ext import commands

class Downtown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[923357625138155541])  # Create a slash command for the supplied guilds.
    async def ud(self, ctx):
        await ctx.respond("Hi, this is a slash command from a cog!")

def setup(bot):
    bot.add_cog(Downtown(bot))

