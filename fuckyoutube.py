import re
from pytube import YouTube

def get_direct_link(youtube_url, selected_quality=None):
    try:
        yt = YouTube(youtube_url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        if not streams:
            return "could not find anything"
        
        if selected_quality:
            selected_streams = [s for s in streams if selected_quality in s.resolution]
            if selected_streams:
                stream = selected_streams[0]
            else:
                return f"selected quality '{selected_quality}' not available. available resolutions: {', '.join([s.resolution for s in streams])}"
        else:
            stream = yt.streams.get_highest_resolution()
            
        direct_link = stream.url
        return direct_link
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    youtube_url = input("url: ")
    
    yt = YouTube(youtube_url)
    available_qualities = [s.resolution for s in yt.streams.filter(progressive=True, file_extension="mp4")]
    print("available resolutions:")
    for quality in available_qualities:
        print(quality)
    
    selected_quality = input("enter the desired resolution (or press ENTER for the highest resolution): ")
    
    direct_link = get_direct_link(youtube_url, selected_quality)
    
    if direct_link:
        print("direct link:\n")
        print(direct_link)
    else:
        print("could not retrieve")
