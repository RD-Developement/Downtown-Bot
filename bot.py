import discord
from discord.ui import Button, View
from discord.ext import commands
from dotenv import load_dotenv
from os import environ
import os
from discord.commands import permissions
import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", description="description", intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('{0.user} is online'.format(bot))

class WelcomeButton(View):
    @discord.ui.button(label="Say welcome!", emoji="<:idkwelcomething:926472273626529922>", style=discord.ButtonStyle.blurple)
    async def button_callback(self, button, interaction):
        user = interaction.user
        await interaction.response.send_message(f'{user.mention} welcomes a new member to {user.guild.name}!')

@bot.event
async def on_member_join(member):
    if member.guild.id == 771797312581402674:
        channel = bot.get_channel(824363941966250046)
        member_role = member.guild.get_role(795096734303780935)
        special_role = member.guild.get_role(819644879796699196)
        level_role = member.guild.get_role(819640864669696060)

        em = discord.Embed(title= "Welcome " + member.display_name + "!", description=f"Welcome to the Relaxed side of Discord, **" + member.display_name + "**! \n Dont forget to check out:\n" + member.guild.get_channel(806194833852858378).mention + "\n" + member.guild.get_channel(818131977122480148).mention + "\n" + member.guild.get_channel(818964691945652246).mention +"\n", color=discord.Colour.purple())
        em.set_thumbnail(url='http://bot.relaxed-downtown.com/img/server-icon.gif')
        em.timestamp=datetime.datetime.utcnow()
        em.set_footer(text="Downtown Bot", icon_url="https://bot.relaxed-downtown.com/img/bot-icon.png")
        
        view=WelcomeButton()
        await channel.send(content=f"{member.mention}", embed=em, view=view)
        await member.add_roles(member_role)
        await member.add_roles(special_role)
        await member.add_roles(member_role)
    else:
        return
        
load_dotenv(".env")
bot.run(environ.get("TOKEN"))