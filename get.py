from moviepy.editor import *
from pytube import YouTube
from pprint import pprint
import sys
 
url = sys.argv[1]
pprint(url)

yt = YouTube(url)
pprint(yt)

yt.streams.first().download('/Users/jpjuliao/Projects/python-youtube-downloader')

# video = VideoFileClip("myHolidays.mp4").subclip(50,60)
# video.write_videofile("myHolidays_edited.webm",fps=25)