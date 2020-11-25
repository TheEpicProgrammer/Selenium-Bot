import discord
from discord.ext import commands

import re


class MessageEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.number_pattern = re.compile("(\d+)(?: ?-.+)?") # for counting

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # Prevent bot from responding to itself
        if user == self.bot.user: return

       #if reaction.message.id == :


def setup(bot):
    bot.add_cog(MessageEventCog(bot))