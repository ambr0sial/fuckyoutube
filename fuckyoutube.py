import re
from pytube import YouTube

def get_direct_link(youtube_url):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        direct_link = stream.url
        return direct_link
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    youtube_url = input("url: ")
    
    direct_link = get_direct_link(youtube_url)
    
    if direct_link:
        print("direct link:")
        print(direct_link)
    else:
        print("could not retrieve the link")