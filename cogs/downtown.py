from discord.commands import slash_command
from discord.ext import commands
import discord

class Downtown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        vip = after.guild.get_role(925010211331248129)
        if vip in after.roles and vip not in before.roles:
            completed_all_levels = after.guild.get_role(925010321947643917)
            await after.edit(nick=f'🌟 {after.display_name}')
            
            em = discord.Embed(title="Congrats On VIP!", description="You just reached the VIP status on Relaxed Downtown! There are many features that come with VIP, such as:", color=discord.Colour.purple())
            em.add_field(name="Perks", value="> ➜ You will be rewarded with the @VIP's role \n ➜ You can change your nickname in 🎀︱request-a-nick \n ➜ You can choose a color role in 🎨︱color-roles \n ➜ You get access to exclusive chats and VC's (🥥︱beach-party / 🚤︱Yacht Club)") 

            # await after.send('```Hey! You! Yeah You! 😎\n\nLets go you just reached the VIP Status on Relaxed Downtown! 💜 \nAnd Yes we have some Premium features on Relaxed Downtown for VIP users: \n \n-Hidden VIP Chats ⭐ (You can find the VIP category under the Minigames category) \n \n-You can now request a nickname! (The text channel for that can be found in the Support category) 🦋\n \n-Question Of The Day :question: (Can be found in the Off-Topic Category) \n \n-Color Roles (can be found in the category User info) ```')
            await after.send(embed=em)
            await after.add_roles(completed_all_levels)
            
def setup(bot):
    bot.add_cog(Downtown(bot))