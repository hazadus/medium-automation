# https://python.plainenglish.io/10-python-mini-automation-projects-177cbd01f0a4
# pip3 install pytube
from pytube import YouTube


def downloader(url):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    print("video downloaded")


downloader("youtube.com/watch?v=FgYYWn5XEys")
