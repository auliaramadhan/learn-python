import os
import re
from unicodedata import name
from pip import main
from pytube import Playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLJ70FsLLPuxOx-RWCjX7OtHzpeE_rPsMc'
playlist = Playlist(playlist_url)   
DOWNLOAD_DIR = f'H:\Download - HDD\{playlist.title}'
os.makedirs(DOWNLOAD_DIR)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
print(len(playlist.video_urls))    
for url in playlist.video_urls:
    print(url)    
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(DOWNLOAD_DIR)
