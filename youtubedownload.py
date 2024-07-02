

from pytube import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    return yt

# for video_path in ['https://www.youtube.com/shorts/pyAEaJTE2Y0', 'https://www.youtube.com/shorts/wS50UK8wvUE']:
#     try:
#         print(downloadYouTube(video_path, 'videos'))
#     except:
#         pass