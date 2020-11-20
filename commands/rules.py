import discord
from discord.ext import commands

import utils.TextUtil
import utils.RulesUtil


class RulesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='rules', aliases=['rule'])
    async def rules(self, ctx, command: str, *args):
        if not 764121607081426945 in list(map(lambda r:r.id,ctx.message.author.roles)):
            await TextUtil.blink("You do not have the `wheel` role.")
    
        channel = self.bot.get_channel(737096170043605032)
        authorid = ctx.message.author.id
        isRulesChannel = ctx.message.channel.id == 737096170043605032
    
        if isRulesChannel:
            await ctx.message.delete()
    
        rules = rules_get()
    
        if command == "init":
            if not "new" in args:
                for id in rules["ids"]:
                    msg = await channel.fetch_message(rules["ids"][id])
                    await msg.delete()
    
            for topic in rules:
                if topic == "ids": continue
    
                em = discord.Embed(title=f"{topic.title()} Rules", color=0x52c832)
                for num in rules[topic]:
                    em.add_field(
                        name=f"Rule {num}", value=rules[topic][num], inline=True)
                msg = await channel.send(embed=em)
    
                rules["ids"][topic] = msg.id
    
            if not isRulesChannel:
                await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
    
        elif command == "add":
            # rules add <string-topic> <string-rule>
            if len(args) == 1:
                if args[0] in rules:
                    await TextUtil.blink("category already exists")
                    return
                rules[args[0]] = {}
                em = discord.Embed(
                    title=f"{args[0].title()} Rules", color=0x52c832)
                msg = await channel.send(embed=em)
                rules["ids"][args[0]] = msg.id
            elif len(args) > 1:
                if args[0] != "ids" and not args[0] in rules:
                    await TextUtil.blink(f"category '{args[0]}' does not exist")
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
    
                    msg = await channel.fetch_message(rules["ids"][args[0]])
                    await msg.edit(embed=em)
    
                    if not isRulesChannel:
                        await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
                else:
                    await TextUtil.blink("Non-existent category")
                    return
            else:
                await TextUtil.blink("Not enough arguments")
                return
    
        elif command == "edit":
            # rules edit <string-topic> <int-id> <string-rule>
            if len(args) > 2:
                rules[args[0]][args[1]] = ' '.join(args[2:])
            else:
                if not isRulesChannel:
                    await ctx.send("Not enough arguments")
                return
    
            if args[0] != "ids" and (match := findClosest(args[0], rules, 50)):
                if args[0] != match:
                    msg = await ctx.send(f"Do you mean: `{match}`?")
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
    
                msg = await channel.fetch_message(rules["ids"][args[0]])
                await msg.edit(embed=em)
    
                if not isRulesChannel:
                    await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
            else:
                await TextUtil.blink("Non-existent category")
                return
    
        elif command in ["delete", "del"]:
            # rules delete <string-topic> <int>
    
            if args[0] != "ids" and not args[0] in rules:
                await TextUtil.blink(f"category '{args[0]}' does not exist")
                return
    
            if len(args) == 1:
                react = await wait_react(ctx, bot, ctx.message.author.mention+" Are you sure you want to delete this category?", ["✅","❌"], True)
                if react == "✅":
                    rules_backup(rules, authorid)
        
                    rules.pop(args[0])
        
                    msg = await channel.fetch_message(rules["ids"][args[0]])
                    await msg.delete()
        
                    rules["ids"].pop(args[0])
    
            elif len(args) == 2:
                rules_backup(rules, authorid)
    
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
    
                msg = await channel.fetch_message(rules["ids"][args[0]])
                await msg.edit(embed=em)
    
                if not isRulesChannel:
                    await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
    
            else:
                await TextUtil.blink("Not enough arguments")
                return
    
        elif command == "json":
            await ctx.send("https://repl.it/@AlexAirbus380/SeleniumBOT#rules.json")
    
        elif command == "backup":
            rules_backup(rules, authorid)
    
        else:
            await TextUtil.blink(f"Unknown command '{command}'")
            return
    
        rules_dump(rules)

def setup(bot):
    bot.add_cog(RulesCog(bot))