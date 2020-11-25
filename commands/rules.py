import discord
from discord.ext import commands

import utils.TextUtil as TextUtil
import utils.JsonUtil as JsonUtil


class RulesCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='rules', aliases=['rule'])
    async def rules(self, ctx, command: str, *args):

        if not 764121607081426945 in list(map(lambda r: r.id, ctx.message.author.roles)):
            await TextUtil.blink("You do not have the `wheel` role.", ctx.message)
    
        channel = self.bot.get_channel(737096170043605032)
        authorid = ctx.message.author.id
        isRulesChannel = ctx.message.channel.id == 737096170043605032
    
        if isRulesChannel:
            await ctx.message.delete()
    
        rules = RulesUtil.get("rules", "rules")
        ids = RulesUtil.get("rules", "ids")
    
        if command == "init":
            if not "new" in args:
                for id in ids.values():
                    msg = await channel.fetch_message(id)
                    await msg.delete()
    
            for topic in rules:
                if topic == "ids": continue
    
                em = discord.Embed(title=f"{topic.title()} Rules", color=0x52c832)
                for num in rules[topic]:
                    em.add_field(
                        name=f"Rule {num}", value=rules[topic][num], inline=True)
                msg = await channel.send(embed=em)
    
                ids[topic] = msg.id
    
            if not isRulesChannel:
                await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
    
        elif command == "add":
            # Create category
            if len(args) == 1:
                if args[0] in rules:
                    await TextUtil.blink("Category already exists")
                    return

                rules[args[0]] = {}
                em = discord.Embed(
                    title=f"{args[0].title()} Rules", color=0x52c832)

                msg = await channel.send(embed=em)
                ids[args[0]] = msg.id
                
            # Add rule to category
            elif len(args) > 1:
                if args[0] == "ids" and not args[0] in rules:
                    await TextUtil.blink(f"Category '{args[0]}' does not exist")
                    return
    
                rules[args[0]][str(len(rules[args[0]]) + 1)] = ' '.join(args[1:])
    
                if args[0] != "ids" and args[0] in rules:
                    em = discord.Embed(
                        title=f"{args[0].title()} Rules", color=0x52c832)

                    for num in rules[args[0]]:
                        em.add_field(
                            name=f"Rule {num}",
                            value=rules[args[0]][num],
                            inline=True)
    
                    msg = await channel.fetch_message(ids[args[0]])
                    await msg.edit(embed=em)

                else:
                    await TextUtil.blink("Non-existent category")
                    return
            
            # 0 arguments
            else:
                await TextUtil.blink("Not enough arguments")
                return
            
            if not isRulesChannel:
                await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
    
        elif command == "edit":
            # rules edit <string-topic> <int-id> <string-rule>
            if len(args) > 2:
                rules[args[0]][args[1]] = ' '.join(args[2:])
            else:
                if not isRulesChannel:
                    await ctx.send("Not enough arguments")
                return
    
            if args[0] != "ids" and (match := TextUtil.findClosest(args[0], rules, 50)):
                if args[0] != match:
                    msg = await ctx.send(f"Did you mean: `{match}`?")
                    await msg.add_reaction("\N{WHITE HEAVY CHECK MARK}")
    
                    for _ in range(10):
                        pass
    
                em = discord.Embed(
                    title=f"{args[0].title()} Rules", color=0x52c832)
                for num in rules[args[0]]:
                    if num == args[1]:
                        rules[args[0]][args[1]] = ' '.join(args[2:])
                        em.add_field(
                            name=f"Rule {num}",
                            value=' '.join(args[2:]),
                            inline=True)
                    else:
                        em.add_field(
                            name=f"Rule {num}",
                            value=rules[args[0]][num],
                            inline=True)
    
                msg = await channel.fetch_message(ids[args[0]])
                await msg.edit(embed=em)

            else:
                await TextUtil.blink("Non-existent category")
                return
            
            if not isRulesChannel:
                await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
    
        elif command in ["delete", "del"]:
            # rules delete <string-topic> <int>
    
            if args[0] == "ids" and not args[0] in rules:
                await TextUtil.blink(f"Category '{args[0]}' does not exist")
                return
    
            if len(args) == 1:
                react = await TextUtil.wait_react(ctx, self.bot, ctx.message.author.mention+" Are you sure you want to delete this category?", ["✅","❌"], True)
                if react == "✅":
                    RulesUtil.rules_backup(rules, authorid)
        
                    rules.pop(args[0])
        
                    msg = await channel.fetch_message(ids[args[0]])
                    await msg.delete()
        
                    ids.pop(args[0])
    
            elif len(args) == 2:
                react = await TextUtil.wait_react(ctx, self.bot, ctx.message.author.mention+" Are you sure you want to delete this rule?", ["✅","❌"], True)
                if react == "✅":
                    RulesUtil.rules_backup(rules, authorid)
        
                    em = discord.Embed(
                        title=f"{args[0].title()} Rules", color=0x52c832)
        
                    rules[args[0]].pop(args[1])
                    rules[args[0]] = {
                        str(i + 1): list(rules[args[0]].values())[i]
                        for i in range(len(rules[args[0]]))
                    }
        
                    for num in rules[args[0]]:
                        em.add_field(
                            name=f"Rule {num}", value=rules[args[0]][num], inline=True)
        
                    msg = await channel.fetch_message(ids[args[0]])
                    await msg.edit(embed=em)
        
                    if not isRulesChannel:
                        await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
    
            else:
                await TextUtil.blink("Not enough arguments")
                return
    
        elif command == "json":
            await ctx.send("https://repl.it/@AlexAirbus380/SeleniumBOT#rules.json")
    
        elif command == "backup":
            RulesUtil.rules_backup(rules, authorid)
    
        else:
            await TextUtil.blink(f"Unknown command '{command}'")
            return
    
        RulesUtil.dump({"rules": rules, "ids": ids})

def setup(bot):
    bot.add_cog(RulesCog(bot))