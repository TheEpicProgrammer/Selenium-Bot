import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


class HelpCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx, category=None):
        embed = None
        
        if not category:
            embed=discord.Embed(title="Commands List", color=0x52c832)
            # embed.add_field(name="emoji category", value="`;help category`", inline=True)
            embed.add_field(name=":scroll: Rules", value="`;help rules`", inline=True)
            embed.add_field(name=":notes: Music", value="`;help music`", inline=True)
            embed.add_field(name=":video_game: Fun", value="`;help fun`", inline=True)
            embed.add_field(name=":speech_balloon: Messages", value="`;help message`", inline=True)
            
        
        else:
            match = TextUtil.findClosest(category, ["rules", "music", "fun", "message"], 60)
            
            if not match:
                await ctx.send(f"Unknown category: `{category}`")
                return
    
            if match == "rules":
                embed=discord.Embed(title="Rules Help", color=0x52c832)
                embed.add_field(name="rules init (new)", value="Initializes rules. If `new` is added, it won't delete previous set of rules.", inline=True)
                embed.add_field(name="rules add <category> <rule>", value="Adds a new rule to a given category.", inline=True)
                embed.add_field(name="rules edit <category> <id> <newrule>", value="Edits a preexisting rule by its id.", inline=True)
                embed.add_field(name="rules delete <category> (id)", value="Deletes a specific rule when id is given or a whole category. A backup is made automatically.", inline=True)
        
            elif match == "music":
                embed=discord.Embed(title="Music Help", color=0x52c832)
                embed.add_field(name="music play <song>", value="Joins the bot to your channel and plays the given song.", inline=True)
                embed.add_field(name="music list", value="Lists all available songs.", inline=True)
                
            elif match == "fun":
                embed=discord.Embed(title="Fun Help", color=0x52c832)
                embed.add_field(name="._.", value="(._. )", inline=True)
                embed.add_field(name="portnuber", value="I never remember it...", inline=True)
                embed.add_field(name="test", value="A command used for testing. No good help message can be made for this one. <developers only>", inline=True)
            
            elif match == "message":
                embed=discord.Embed(title="Fun Help", color=0x52c832)
                embed.add_field(name="getmsg", value="Get's all messages from a channel.", inline=True)
                embed.add_field(name="msgquery", value="Queries messages from a channel.", inline=True)
                embed.add_field(name="emoji", value="Prints out all the emojis in the server.", inline=True)
        
        if not embed:
            await ctx.send(f"Unknown category: `{category}`")
            return
            
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))