import requests
import re

def get_direct_link(youtube_url):
    try:
        response = requests.get(youtube_url)
        if response.status_code == 200:
            match = re.search(r'"url":"(https://[^"]+)"', response.text)
            if match:
                direct_link = match.group(1)
                return direct_link
            else:
                return "not found"
        else:
            return f"failed to fetch the youtube page (http {response.status_code})."
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    youtube_url = input("url: ")
    
    direct_link = get_direct_link(youtube_url)
    
    if direct_link:
        print("direct link:")
        print(direct_link)
    else:
        print("could not retrieve")
