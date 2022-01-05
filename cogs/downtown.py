from discord.commands import slash_command
from discord.ext import commands
import discord
import datetime

class Downtown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        vip = after.guild.get_role(795321686517874698)
        if vip in after.roles and vip not in before.roles:
            completed_all_levels = after.guild.get_role(839522086506856528)
            
            em = discord.Embed(title="Congrats On VIP!", description="You just reached the VIP status on Relaxed Downtown!", color=discord.Colour.purple())
            em.add_field(name="Rewards", value=f"There are many rewards that you get with VIP, such as: \n > ➜ You will be rewarded with the @VIP's role \n> ➜ You can change your nickname in 🎀︱request-a-nick \n > ➜ You can choose a color role in 🎨︱color-roles \n > ➜ You get access to exclusive chats and VC's (🥥︱beach-party / 🚤︱Yacht Club)", inline=False) 
            em.set_thumbnail(url="https://bot.relaxed-downtown.com/img/server-icon.png")
            em.set_footer(text="Downtown Bot", icon_url="https://bot.relaxed-downtown.com/img/bot-icon.png")

            await after.send(embed=em)
            await after.add_roles(completed_all_levels)
            
def setup(bot):
    bot.add_cog(Downtown(bot))