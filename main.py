import discord
from discord.ext import commands

import keep_online
import os


keep_online.start()
bot = commands.Bot(command_prefix=';', help_command=None)

exts = ["commands.help",
        "commands.rules",
        "commands.media",
        "commands.fun",
        "commands.minecraft",
        "commands.message",
        "commands.count",
        
        "events.ready",
        "events.message",
        "events.react",
        
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
    embed.add_field(name="Supercolbat#2697", value="0b0t ~~legend~~ player")
    embed.add_field(name="Alex", value="cat")
    embed.add_field(name="Eli", value="am frog **e**")
    await ctx.send(embed=embed)


if __name__ == '__main__':
    for extension in exts:
        bot.load_extension(extension)

bot.run(os.getenv("TOKEN"))