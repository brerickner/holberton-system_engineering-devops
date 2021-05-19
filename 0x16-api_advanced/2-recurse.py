#!/usr/bin/python3
'''Module that queries Reddit API recursively'''

from json.decoder import JSONDecodeError, JSONDecoder
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''Method that returns returns a list containing the titles of
       all hot articles for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    '''page through the listings with after anchoring result'''
    parameter = {'limit': 100, 'after': after}
    headers = {"User-Agent": "change username"}
    try:
        response = requests.get(
                                url,
                                headers=headers,
                                params=parameter,
                                allow_redirects=False).json()
    except JSONDecodeError:
        return(None)
    meow = response.get('data')
    children = meow.get('children')
    after = meow.get('after')
    flag = 0
    for titles in children:
        hot_list.append(titles.get('data')['title'])
        flag += 1
        if after is None:
            return(hot_list)
    return(recurse(subreddit, hot_list, after))
