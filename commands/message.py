import discord
from discord.ext import commands
from discord.utils import get
import time
import random

import utils.TextUtil as TextUtil


class MessageCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getmsg")
    async def getmsg(self, ctx, channel: discord.TextChannel):
        loadingmsg = await TextUtil.sendLoading(ctx.channel)
        start = time.time()
    
        messages = await channel.history(limit=None).flatten()
        length = len(messages)
        chosenmsg = random.choice(messages)
    
        embed=discord.Embed(color=0xa80000)
        embed.set_thumbnail(url=chosenmsg.author.avatar_url)
        embed.add_field(name=f"Typed by {chosenmsg.author}", value=f"{chosenmsg.content}\n\n{chosenmsg.jump_url}", inline=False)
        await loadingmsg.edit(content=f"||{ctx.message.author.mention}||\n\nTime: **{time.time()-start} seconds**\nChose from {length} message{'s' if length else ''}", embed=embed)
    
    
    @commands.command(name="msgquery")
    async def msgquery(self, ctx, channel: discord.TextChannel, *args):
        args = ' '.join(args)

        start = time.time()
        embed=discord.Embed(color=0xa80000)
        
        loadingmsg = await TextUtil.sendLoading(ctx.channel)
        messages = await channel.history(limit=None).flatten()
        length = len(messages)
        counter = 0
        # chosenmsg = []

        for i in messages:
            if args in i.content:
                embed.add_field(name=f"{i.author.display_name}", value=i.content)
                # chosenmsg.append(i.content)
                counter += 1
        
        # {chosenmsg.content}\n{chosenmsg.jump_url}", inline=False)
        await loadingmsg.edit(content=f"\n\nTime: **{time.time()-start} seconds**\nLooked through {length} message{'s' if length else ''}\n Found {counter} occurances of {args}", embed=embed)
    
    @commands.command(name="emojis")
    async def emojis(self, ctx):
        emojis = [
            f"<{'a' if e.animated else ''}:{e.name}:{e.id}>"
            for e in 
            ctx.message.guild.emojis
        ]
        await ctx.send(' '.join(emojis))
        

def setup(bot):
    bot.add_cog(MessageCog(bot))
    