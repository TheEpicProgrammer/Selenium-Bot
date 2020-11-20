import discord
from discord.ext import commands

import asyncio
import random


async def initMOTD(bot):
    while True:
        channel = bot.get_channel(763388283241496597)
        messages = await channel.history(limit=None).flatten()
        chosenmotd = random.choice(messages).content

        if chosenmotd.startswith('**watch**'):
            activity = discord.Activity(
                name=chosenmotd[10:], type=discord.ActivityType.watching)
            await bot.change_presence(activity=activity)

        elif chosenmotd.startswith('**listen**'):
            activity = discord.Activity(
                name=chosenmotd[11:], type=discord.ActivityType.listening)
            await bot.change_presence(activity=activity)
            
        else:
            await bot.change_presence(activity=discord.Game(name=chosenmotd))

        await asyncio.sleep(5)


class ReadyEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has logged into discord')
        print("Bot is ready")
        await self.bot.change_presence(activity=discord.Game(name="Bot is ready"))

        await asyncio.sleep(5)
        await initMOTD(self.bot)
    

def setup(bot):
    bot.add_cog(ReadyEventCog(bot))