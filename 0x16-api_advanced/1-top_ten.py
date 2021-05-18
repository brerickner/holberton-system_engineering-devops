#!/usr/bin/python3
""" Module that queries Reddit API """

import requests
from sys import argv


def top_ten(subreddit):
    """ Method that  prints the titles of the first 10 hot posts
    listed for a given subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "change username"}
    try:
        response = requests.get(
                                url,
                                headers=headers,
                                allow_redirects=False).json()
        meow = response.get('data')
        children = meow.get('children')
        for titles in children[:10]:
            print(titles.get('data')['title'])
    except:
        print("None")
