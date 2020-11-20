import discord
from discord.ext import commands


class MessageEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: return

        if "creeper" in message.content.lower():
            msg = await message.channel.send("aw man")
            await asyncio.sleep(1)
            await msg.delete()
        elif "aw man" in message.content.lower():
            msg = await message.channel.send("creeper")
            await asyncio.sleep(1)
            await msg.delete()


def setup(bot):
    bot.add_cog(MessageEventCog(bot))