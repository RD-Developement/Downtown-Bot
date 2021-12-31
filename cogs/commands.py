from discord.commands import slash_command
from discord.ext import commands
import discord
from discord.ext.commands.cooldowns import BucketType
import datetime

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[771797312581402674])
    async def welcome(self, ctx, member: discord.Member):
        '''Welcomes a member to the server!'''
        await ctx.respond(f'{ctx.author.mention} welcomes {member.mention} to {ctx.guild.name}!')

    @slash_command(guild_ids=[771797312581402674])
    @commands.has_permissions(manage_messages=True)
    async def revive(self, ctx, topic=None):
        '''Revives the chat every 30 minutes'''
        if topic == None:
            revive = discord.utils.get(ctx.guild.roles, id=831686382698102844)
            await ctx.respond("The chat has been revived!", ephemeral=True)
            await ctx.send(f"{revive.mention} The chat's dead, come back and revive it!")
        else:
            em=discord.Embed(title=f"{ctx.author.display_name}'s Topic Is", description=f'{topic}', color=discord.Colour.blurple())
            em.set_thumbnail(url="https://bot.relaxed-downtown.com/img/bot-icon.png")
            em.timestamp=datetime.datetime.utcnow()
            em.set_footer(text="Downtown Bot", icon_url="https://bot.relaxed-downtown.com/img/bot-icon.png")
            revive = discord.utils.get(ctx.guild.roles, id=831686382698102844)
            await ctx.send(f"{revive.mention}")
            await ctx.respond(embed=em)

def setup(bot):
    bot.add_cog(Commands(bot))