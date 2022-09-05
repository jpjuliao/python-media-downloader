from moviepy.editor import *
from pytube import YouTube
from pytube.cli import on_progress

from pprint import pprint
import sys
 
url = sys.argv[1]
pprint(url)

def progress_function(stream, chunk, file_handle, bytes_remaining):
    print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')

yt = YouTube(url, on_progress_callback=on_progress)
pprint(yt)

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# yt.streams.first().download('/Users/jpjuliao/Projects/python-youtube-downloader')

# video = VideoFileClip("myHolidays.mp4").subclip(50,60)
# video.write_videofile("myHolidays_edited.webm",fps=25)