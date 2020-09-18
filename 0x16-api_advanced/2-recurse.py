#!/usr/bin/python3
"""
This script queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = 'https://www.reddit.com/r/'
    url = url + subreddit + '/hot.json?limit=100&after=' + after
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        list_dicts = data.get('data').get('children')
        for dict in list_dicts:
            hot_list.append(dict['data']['title'])
        after = data.get('data').get('after')
        if after is None:
            return (hot_list)
        return recurse(subreddit, hot_list, after)
