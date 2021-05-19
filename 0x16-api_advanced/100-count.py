#!/usr/bin/python3
""" Module that queries Reddit API recursively """

import requests
import sys


def count_words(subreddit, word_list, after=None, word_dict={}, flag=0):
    """ Method that returns returns a list containing the titles of
    all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    ''' page through the listings with after anchoring with "" '''
    parameter = {'limit': 100, 'after': after}
    headers = {"User-Agent": "change username"}
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
        title_fetch = titles.get('data')['title'].lower()
        for word in word_list:
            if word in title_fetch:
                flag += 1
                word_dict[word] = flag
    if after is None:
        for x in word_dict.keys():
            print("{}: {}".format(x, word_dict[x]))
        return
    return(count_words(subreddit, word_list, after, word_dict, flag))
