import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


class CountCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="count", aliases=["number"])
    async def count(self, ctx, command, *args):
        if command == "leaderboard": loadingmsg = await TextUtil.sendLoading(ctx.channel)

        channel = self.bot.get_channel(776554955418501141)
        messages = await channel.history(limit=None).flatten()
        
        if command == "leaderboard":

            leaderboard = {}
            for m in messages:
                leaderboard[m.author] = leaderboard[m.author] + 1 if m.author in leaderboard else 1

            leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1])[::-1]}  # https://stackoverflow.com/a/613218
    
            embed = discord.Embed(title="Counting leaderboard", color=0x64f7b7)
            for l in leaderboard.items():
                embed.add_field(name=l[0], value=f"Counted **{l[1]}** time{'s' if l[1] > 1 else ''}", inline=False)

            await loadingmsg.edit(content="", embed=embed)


def setup(bot):
    bot.add_cog(CountCog(bot))