#!/usr/bin/python3
""" Module that queries Reddit API recursively """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Method that returning list of hot subreddits """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    parameter = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'change username'}
    response = requests.get(
        url,
        headers=headers,
        params=parameter,
        allow_redirects=False)
    if response.status_code != 200:
        return(None)
    response = response.json()
    meow = response.get('data')
    children = meow.get('children')
    after = meow.get('after')
    for titles in children:
        hot_list.append(titles.get('data')['title'])
    if after is None:
        return(hot_list)
    return(recurse(subreddit, hot_list, after))
