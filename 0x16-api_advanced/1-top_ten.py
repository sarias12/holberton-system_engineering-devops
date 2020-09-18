#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('None')
    else:
        data = response.json()
        list_dicts = data.get('data').get('children')
        for dict in list_dicts:
            print(dict['data']['title'])
