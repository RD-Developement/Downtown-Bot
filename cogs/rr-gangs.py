from discord.commands import slash_command
from discord.ext import commands
import discord
from discord.commands import permissions
import datetime 
from discord.utils import get
from discord.ui import Button, View

class Gangs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[771797312581402674])
    @permissions.permission(user_id=721341252649353256, permission=True)
    async def gangs(self, ctx):
        pcGangButton = Button(label="PC Gang", style=discord.ButtonStyle.blurple, emoji="<:pcgang:926869314877923359>")
        psGangButton = Button(label="PS4 Gang", style=discord.ButtonStyle.blurple, emoji="<:psicon:926870430340485212>")
        xbGangButton = Button(label="Xbox Gang", style=discord.ButtonStyle.blurple, emoji="<:xboxicon:926870769957470299>")
        swGangButton = Button(label="Switch Gang", style=discord.ButtonStyle.blurple, emoji="<:switchicon:926871101659807744>")

        async def pcCallback(self, interaction):
            user = interaction.user
            role = interaction.guild.get_role(818164649198878730)

            if role is None:
                return

            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(
                    f"✅ You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True)        
            
            # async def psCallback(self, interaction: discord.Interaction):
            #     user = interaction.user
            #     role = interaction.guild.get_role(818164649198878730)

            #     if role is None:
            #         return

            #     if role not in user.roles:
            #         await user.add_roles(role)
            #         await interaction.response.send_message(
            #             f"✅ You have been given the role {role.mention}", ephemeral=True)
            #     else:
            #         await user.remove_roles(role)
            #         await interaction.response.send_message(
            #             f"❌ The {role.mention} role has been taken from you", ephemeral=True)

        pcGangButton.callback = pcCallback

        view=View()
        view.add_item(pcGangButton)
        view.add_item(psGangButton)
        view.add_item(xbGangButton)
        view.add_item(swGangButton)
        
        em=discord.Embed(title="Gangs", description="<:pcgang:926869314877923359> ➜ PC Gang\n <:psicon:926870430340485212> ➜ PS Gang\n <:xboxicon:926870769957470299> ➜ XBOX Gang\n <:switchicon:926871101659807744> ➜ Switch Gang", color=discord.Colour.purple())
        em.set_thumbnail(url="https://bot.relaxed-downtown.com/img/bot-icon.png")
        em.set_footer(text="Downtown Bot", icon_url="https://bot.relaxed-downtown.com/img/bot-icon.png")

        await ctx.respond(embed=em, view=view)

def setup(bot):
    bot.add_cog(Gangs(bot))