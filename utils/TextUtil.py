import discord
from discord.ext import commands

import asyncio
from fuzzywuzzy import process


def findClosest(string, options, margin=75):
    match = process.extractOne(string, [*options])
    print(f'{string} => {options}  {match[0]} ({match[1]}%)')
    return match[0] if match[1] >= margin else False


async def wait_react(ctx, bot, msg, emojis, delete=False):
    target = await ctx.send(msg)
    for e in emojis: await target.add_reaction(e)

    def check(reaction, user):
        return reaction.message.id == target.id and user == ctx.message.author and str(reaction.emoji) in emojis

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        return False
    else:
        if delete: await target.delete()
        return reaction.emoji


async def blink(message, wait=3, forcedel=False):
    msg = await message.channel.send(message)
    await asyncio.sleep(wait)

    if forcedel or ctx.message.channel.id == 737096170043605032:
        await msg.delete()