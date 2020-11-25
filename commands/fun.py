import discord
from discord.ext import commands

from fuzzywuzzy import process
import os
import typing
import asyncio
import random


class FunCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.lastcat = None
        

    @commands.command(name="portnuber")
    async def portnuber(self, ctx):
        embed = discord.Embed(title="Port Nuber", color=0x2F4186)
        embed.add_field(name='Port Nuber', value='E')
        embed.add_field(
            name='25565 or something it is just the default i think',
            value='What is it though?')
        embed.set_footer(text='Port Nuber Service')
        await ctx.send(embed=embed)
    

    @commands.command(name="._.")
    async def wut(self, ctx, times:typing.Optional[int]=3):
        # await ctx.message.delete()
    
        sp=[""," "]
        msg = await ctx.send("("+"._.".join(sp)+")")
    
        for _ in range(times-1):
            await asyncio.sleep(1)
            sp = [sp[1],sp[0]]
            await msg.edit(content="("+"._.".join(sp)+")")
    

    @commands.command(name="cat", aliases=["dog", "joj"])
    async def cat(self, ctx):
        files = os.listdir("files/images/cats")
        while (f:=random.choice(files)) != self.lastcat:
            self.lastcat = f
            catPicture = discord.File(f"files/images/cats/{f}")
            await ctx.send(file=catPicture)
            break
    

    @commands.command(name="lev")
    async def lev(self, ctx, st, *ops):
        match = process.extractOne(st, ops)
        await ctx.send(f"{st} is {match[1]}% similar to {match[0]}")


    @commands.command(name="deletethis")
    async def deletethis(self, ctx, time=1):
        await ctx.message.delete(delay=time)

def setup(bot):
    bot.add_cog(FunCog(bot))