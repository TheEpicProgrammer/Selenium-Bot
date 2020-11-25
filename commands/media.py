import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

import pytube
import youtube_dl
import ffmpeg
import pafy
import os

import utils.TextUtil as TextUtil
import utils.MediaUtil as MediaUtil


def get_songs(ext=False):
    return list(map(lambda s:s.split('.')[0] if ext else s, os.listdir("files/music")))


class MediaCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.voice = None
        self.queue = []
    

    @commands.command(name='ytdl')
    async def ytdl(self, ctx, url):
        loadingmsg = await ctx.send("<a:loading:778279344346234941>")
        yt = pytube.YouTube(url)
        video = pafy.new(url)

        title = video.title
        best = video.getbest(preftype="mp4")
        # output = best.download(filepath="files/video/" + video.title.replace(' ', '').replace('/', '') + "." + best.extension, quiet=False)
        d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
        d_video.download("files/video/")
        
        # vbmsg = await ctx.send(output)
        await ctx.send(f"https://SeleniumBOT.bernygg.repl.co/{video.title.replace(' ', '').replace('/', '')}.{best.extension}")
        await loadingmsg.delete()
        # await vbmsg.delete()
    

    @commands.command(name='music')
    async def music(self, ctx, command, *args):
        # channel = self.bot.get_channel(737093341493198953)
    
        if command == "play":
            channel = ctx.author.voice.channel
            song = ' '.join(args)
    
            # fuzzy match
            match = TextUtil.findClosest(song, get_songs(True))
            if match:
                player = discord.FFmpegPCMAudio(f'files/music/{match}.mp3')
                await ctx.send(f"Playing :notes:  `{match}`")
                self.voice = await channel.connect()
            else:
                await ctx.send(f"Song `{song}` does not exist.")
                return

        elif command == "list":
            f = '\n'.join(list(map(lambda f:'• '+f, get_songs())))
            await ctx.send(f"List of songs:\n```{f}```")
            return

        elif command in ["disconnect", "dc", "leave"]:
            if self.voice:
                await self.voice.disconnect()
            else:
                await ctx.send("Already disconnected.")

            return
        
        elif command == "state":
            await ctx.send(self.voice)
            return
    
        # https://stackoverflow.com/a/62107725 owo
    
        self.voice.play(player, after=None)


def setup(bot):
    bot.add_cog(MediaCog(bot))