#!/usr/bin/python3
""" Module that queries Reddit API """

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Method that returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "change username"}
    try:
        response = requests.get(
                                url,
                                headers=headers,
                                allow_redirects=False).json()
        meow = response.get('data')
        return (meow['subscribers'])
    except:
        return 0

'''if __name__ == '__main__':
    sub_reddit = argv[1]
    number_of_subscribers(sub_reddit)'''
