from moviepy.editor import *
from pytube import YouTube
from pytube.cli import on_progress

from pprint import pprint
import sys
 
print('Loading...')

# file_path = '/Users/jpjuliao/Projects/python-youtube-downloader/twenty one pilots Heathens (from Suicide Squad The Album) [OFFICIAL VIDEO].mp4'
# video = VideoFileClip(file_path).subclip(0,30)
# video.write_videofile("edited.mp4",fps=25)

url = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]

# pprint(url)

def complete_function(stream, file_path):
    print('Download complete:', file_path)

    video = VideoFileClip(file_path).subclip(start,end)
    video.write_videofile("edited.mp4",fps=25)

yt = YouTube(
    url, 
    on_progress_callback=on_progress, 
    on_complete_callback=complete_function
)

# pprint(yt)

print('Downloading: ', yt.title, '~ viewed', yt.views, 'times.')

yt.streams.filter(
  progressive=True, 
  file_extension='mp4'
).order_by('resolution').desc().first().download()
