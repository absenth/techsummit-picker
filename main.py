'''
This thing should have an array of locations.
And randomly select one at a time.
'''

import os
import random
import requests
from dotenv import load_dotenv


def main():
    spot = pickspot()
    announcespot(spot)


def pickspot():
    locations = [
            'abgb', 'sabg', 'woodrows', 'docs',
            'moontower', 'little darlin'
            ]

    return(random.choice(locations))

def announcespot(spot):
    load_dotenv()
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    username = 'Botsenth545'
    avatar_url = os.getenv('DISCORD_AVATAR_URL')
    content = f'I have picked the location: {spot}'
    data = {
            'content': content,
            'username': username,
            'avatar_url': avatar_url
            }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print(f'I have posted the location: {spot} to the chat')
    else:
        print(f'I have failed to send the location {spot} - {response.status_code} {response.text}')


if __name__ == '__main__':
    main()
