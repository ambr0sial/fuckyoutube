import requests
import re
import json

def detect_schema(link):
    if link.startswith('http://') or link.startswith('https://'):
        return link  # return as-is if schema already supplied

    response = requests.head('http://' + link)
    if response.status_code == 200:
        return 'http://' + link  # if successful as http, it's http
    else:
        return 'https://' + link  # if not, it's https

def get_direct_link(youtube_url):
    try:
        response = requests.get(youtube_url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        match = re.search(r'"url":"(https://[^"]+googlevideo[^"]+)"', response.text)  # only get video URLs
        if match:
            direct_link = json.loads(f'"{match.group(1)}"')  # Decode escape sequences
            return direct_link
        else:
            return "not found"
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch the YouTube page: {str(e)}"

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube URL: ")

    direct_link = get_direct_link(detect_schema(youtube_url))

    if direct_link:
        print("Direct link:")
        print(direct_link)
    else:
        print("Could not retrieve the direct link.")
