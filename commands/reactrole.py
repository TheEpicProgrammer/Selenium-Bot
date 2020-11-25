import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


class ReactRoleCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reactrole")
    async def reactrole(self, ctx):
        channel = self.bot.get_channel(776508927843237888)
        await channel.send("React to this message for roles!")


def setup(bot):
    bot.add_cog(HelpCog(bot))