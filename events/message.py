import discord
from discord.ext import commands

import re

import utils.TextUtil as TextUtil
import utils.JsonUtil as JsonUtil


class MessageEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.number_pattern = re.compile("(\d+)(?: ?-.+)?") # for counting

    @commands.Cog.listener()
    async def on_message(self, message):
        # Prevent bot from replying to itself
        if message.author == self.bot.user: return

        # Counting moderation
        if message.channel.id == 776554955418501141:
            match = self.number_pattern.search(message.content)
            numbers = JsonUtil.get("count")

            if match and\
               int(match.group(1)) == (v:=numbers["776554955418501141"]["value"]+1) and\
               message.author.id != numbers["776554955418501141"]["uid"]:
                numbers["776554955418501141"] = {
                    "value": v,
                    "uid": message.author.id
                }

                JsonUtil.dump("count", numbers)
            else:
                await message.delete()
            
        # Blink messages
        if "creeper" in message.content.lower():
            await TextUtil.blink("aw man", message, 1, True)
        elif "aw man" in message.content.lower():
            await TextUtil.blink("creeper", message, 1, True)
        elif "toad" in message.content.lower():
            await TextUtil.blink("frog", message, 1, True)
        


def setup(bot):
    bot.add_cog(MessageEventCog(bot))