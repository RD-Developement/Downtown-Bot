import discord
from discord.ui import Button, View
from discord.ext import commands
from dotenv import load_dotenv
from os import environ
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", description="description", intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('{0.user} is online'.format(bot))

@bot.event
async def on_member_join(member):
    if member.guild.id == 923357625138155541:
        em = discord.Embed(title= "Welcome " + member.display_name + "!", description=f"Welcome to the Relaxed side of Discord, **" + member.display_name + "**! \n Dont forget to check out:\n" + member.guild.get_channel(923357625633099808).mention + "\n" + member.guild.get_channel(923362097746817025).mention + "\n" + member.guild.get_channel(923362875219796091).mention +"\n", color=discord.Colour.purple())

        em.set_thumbnail(url='http://bot.relaxed-downtown.com/img/server-icon.gif')
        em.set_footer(text="Tip: Use /welcome or right click the new member's name, go to apps, and click on welcome to welcome them to the server!")

        channel = bot.get_channel(923362875219796091)

        await channel.send(f"{member.mention}")
        await channel.send(embed=em)

@bot.slash_command(guild_ids=[923357625138155541])
async def welcome(ctx, member: discord.Member):
    '''Welcomes a member to the server!'''
    await ctx.respond(f'{ctx.author.mention} welcomes {member.mention} to {ctx.guild.name}!')

@bot.slash_command(guild_ids=[923357625138155541])
async def hi(ctx):
    button = Button(label="click me!", style=discord.ButtonStyle.green, emoji="⚒️")
    view = View()
    view.add_item(button)
    await ctx.respond("hi", view=view)

load_dotenv(".env")
bot.run(environ.get("TOKEN"))