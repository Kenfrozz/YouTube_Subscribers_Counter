import requests
import json

api_key = "AIzaSyCqlL-F80yt-hL2dOW3SkZLWw7gz5m3vnw" # API anahtarını buraya girin
channel_id = "UClnZnWwZl-w-WmLNEbKTpxg" # kanal kimliğini buraya girin


while True:
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"

    response = requests.get(url)
    data = json.loads(response.text)

    subscriber_count = int(data["items"][0]["statistics"]["subscriberCount"])
    print(f"Abone Sayısı: {subscriber_count}")

