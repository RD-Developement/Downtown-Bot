import discord
from discord.ui import Button, View
from discord.ext import commands
from dotenv import load_dotenv
from os import environ
import os
from discord.commands import permissions

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
    if member.guild.id == 771797312581402674:
        channel = bot.get_channel(824363941966250046)
        em = discord.Embed(title= "Welcome " + member.display_name + "!", description=f"Welcome to the Relaxed side of Discord, **" + member.display_name + "**! \n Dont forget to check out:\n" + member.guild.get_channel(806194833852858378).mention + "\n" + member.guild.get_channel(818131977122480148).mention + "\n" + member.guild.get_channel(818964691945652246).mention +"\n", color=discord.Colour.purple())
        em.set_thumbnail(url='http://bot.relaxed-downtown.com/img/server-icon.gif')
        em.set_footer(text="Tip: Use /welcome to welcome them to the server!")

        welcomeButton = Button(label="Welcome Member", style=discord.ButtonStyle.green)
        
        async def welcomeButton_callback(interaction):
            user = interaction.user
            await interaction.response.send_message(f'{user.mention} welcomes {member.mention} to {user.guild.name}!')

        welcomeButton.callback = welcomeButton_callback

        view=View()
        view.add_item(welcomeButton)
        await channel.send(f"{member.mention}")
        await channel.send(embed=em, view=view)
    else:
        return
        
load_dotenv(".env")
bot.run(environ.get("TOKEN"))