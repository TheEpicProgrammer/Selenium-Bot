import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


class TestCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='test')
    async def test(self, ctx):
        if not 779184892378349618 in list(map(lambda r:r.id,ctx.message.author.roles)):
            await TextUtil.blink("You do not have the `wheel` role. noob. get gud.")
            return
        
        react = await TextUtil.wait_react(ctx, self.bot, ctx.message.author.mention+" Are you sure you want to run the test?", ["✅","❌"], True if "del" in ctx.message.content else False)
        if react and react == "✅":
            embed=discord.Embed(title="Is it really a test?", color=0x52c832)
            embed.add_field(name="testing testing 123!", value="https://discord.com/channels/737093341493198949/743530082047623229/779078856266350644", inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send("okay, cancelling")


def setup(bot):
    bot.add_cog(TestCog(bot))