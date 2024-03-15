import time
from datetime import datetime as d
import time as t
import requests

url = "https://discord.com/api/v8/users/@me/settings"

prev = d.now()
prev = prev.strftime("%Y-%m-%d %H:%M:%S")

def changeStatus(message):
    header = {
        "authorization": "<your token here>"
        # guide to get token in the readme!
    }

    jsonData = {
        "status": "idle",
        "custom_status": {
            "text": message
        }
    }

    request = requests.patch(url, headers=header, json=jsonData)

while True:
    current_time = d.now()
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    if not current_time_str == prev:
        prev = current_time_str

        hour = current_time.hour
        if 6 <= hour < 12:
            greeting = "Good morning"
            emoji = "🌅"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
            emoji = "🕛"
        elif 18 <= hour < 22:
            greeting = "Good evening"
            emoji = "🌆"
        else:
            greeting = "Good night"
            emoji = "🌃"

        formatted_time = current_time.strftime("%I:%M:%S %p")
        message = f"{greeting}!, It's {formatted_time}! {emoji} IST for me"
        changeStatus(message)

    time.sleep(0.5)
