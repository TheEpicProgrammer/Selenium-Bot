import discord
from discord.ext import commands

from mcipc.query import Client


class MinecraftCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='players', aliases=['pl', 'list'])
    async def players(self, ctx, *args):
        await ctx.send("im alive :3")
        with Client('selenium.my.pebble.host', 25583) as client:
            await ctx.send("a")
            full_stats = client.full_stats
            await ctx.send("b")
        
        if full_stats.num_players == 0:
            await ctx.send(f"{0} Online players".format(full_stats.num_players))
            await ctx.send("c")
        else:
            await ctx.send(f"Player list: {0}".format(', '.join(query.players)))
            await ctx.send("d")


def setup(bot):
    bot.add_cog(MinecraftCog(bot))