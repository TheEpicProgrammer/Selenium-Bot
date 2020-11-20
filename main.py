import os

# os.system("python -m pip install -r requirements.txt")

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import keep_alive
import random
import sys
import json


keep_alive.keep_alive()

bot = commands.Bot(command_prefix=';', help_command=None)
TOKEN = os.getenv("TOKEN")

song_queue = []
ydl_opts = {}

exts = ["commands.help",
        "commands.rules",
        "commands.media",
        "commands.fun",
        "commands.minecraft",
        
        "events.message",
        "events.ready",
        
        "commands.test"]


@bot.command(name="shutdown")
async def shutdown(ctx):
    if not 764121607081426945 in list(map(lambda r:r.id,ctx.message.author.roles)):
        await ctx.send("You do not have the `wheel` role.")
        return
    
    await ctx.send("beep boop... Shutting down")
    try:
        await bot.logout()
    except:
        print("EnvironmentError")
        bot.clear()

@bot.command(name="credits", aliases = ["devs", "contributers"])
async def credits(ctx):
    embed=discord.Embed(title="Developers and Contributers!", color=0x52c832)
    embed.add_field(name="Supercolbat#2697", value="im joe biden and i approve this message", inline=True)
    embed.add_field(name="Alex", value="cat", inline=True)
    embed.add_field(name="DolphinBob", value="am frog**e**", inline=True)
    await ctx.send(embed=embed)


if __name__ == '__main__':
    for extension in exts:
        bot.load_extension(extension)

bot.run(TOKEN)