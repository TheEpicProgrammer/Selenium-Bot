import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

from pytube import YouTube
import youtube_dl
import ffmpeg
import pafy

import utils.MediaUtil


class MediaCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='ytdl')
    async def ytdl(self, ctx, url):
        loadingmsg = await ctx.send("<a:loading:778279344346234941>")
        yt = Youtube(url)
        video = pafy.new(url)

        title = video.title
        best = video.getbest(preftype="mp4")
        # output = best.download(filepath="video/" + video.title.replace(' ', '').replace('/', '') + "." + best.extension, quiet=False)
        d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
        d_video.download("files/video/")
        
        # vbmsg = await ctx.send(output)
        await ctx.send(f"https://SeleniumBOT.bernygg.repl.co/{video.title.replace(' ', '').replace('/', '')}.{best.extension}")
        await loadingmsg.delete()
        # await vbmsg.delete()
    

    @commands.command(name='music')
    async def music(self, ctx, command, *args):
        #channel = self.bot.get_channel(737093341493198953)
    
        if command == "play":
            channel = ctx.author.voice.channel
            song = ' '.join(args)
    
            # fuzzy match
            match = findClosest(song, get_songs(True))
            if match:
                player = discord.FFmpegPCMAudio(f'music/{match}.mp3')
                await ctx.send(f"Playing :notes:  `{match}`")
                vc = await channel.connect()
            else:
                await ctx.send(f"Song `{song}` does not exist.")
                return
        elif command == "list":
            songs = get_songs()
            f = '\n'.join(list(map(lambda f:'• '+f, songs)))
            await ctx.send(f"List of songs:\n```{f}```")
            return
        elif command in ["disconnect", "dc", "leave"]:
            await vc.disconnect()
            return
    
        # https://stackoverflow.com/a/62107725 owo
    
        vc.play(player, after=None)


def setup(bot):
    bot.add_cog(MediaCog(bot))