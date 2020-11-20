import discord
from discord.ext import commands


class MessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getmsg")
    async def getmsg(self, ctx, channel: discord.TextChannel):
        loadingmsg = await ctx.send("<a:discord_loading:779085179657781251>")
        start = time.time()
    
        messages = await channel.history(limit=None).flatten()
        length = len(messages)
        chosenmsg = random.choice(messages)
    
        embed=discord.Embed(color=0xa80000)
        embed.set_thumbnail(url=chosenmsg.author.avatar_url)
        embed.add_field(name=f"Typed by {chosenmsg.author}", value=f"{chosenmsg.content}\n{chosenmsg.jump_url}", inline=False)
        await loadingmsg.edit(content=f"||{ctx.message.author.mention}||\n\nTime: **{time.time()-start} seconds**\nChose from {length} message{'s' if length else ''}", embed=embed)
    
    
    @commands.command(name="msgquery")
    async def msgquery(self, ctx, channel: discord.TextChannel, *args):
        start = time.time()
        embed=discord.Embed(color=0xa80000)
        loadingmsg = await ctx.send("<a:loading:778279344346234941>")
        args = ' '.join(args)
        messages = await channel.history(limit=None).flatten()
        length = len(messages)
        chosenmsg = []
        for i in messages:
            if args in i.content:
                embed.add_field(name=f"{i.author.nickname}", value=i.content)
                #chosenmsg.append(i.content)
        
        #{chosenmsg.content}\n{chosenmsg.jump_url}", inline=False)
        await loadingmsg.edit(content=f"\n\nTime: **{time.time()-start} seconds**\nChose from {length} message{'s' if length else ''}", embed=embed)
    
    
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