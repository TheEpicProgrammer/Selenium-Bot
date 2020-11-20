def ytdl(self, link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)

def get_songs(self, noext=True):
    for (dirpath, dirnames, filenames) in os.walk("music"):
        return list(map(lambda f:os.path.splitext(f)[0], filenames)) if noext else filenames