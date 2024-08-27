#!/usr/bin/python3

"""
this script queries the reddit api 
for the titles of first 10 hot posts on a subreddit
"""
import requests

def top_ten(subreddit):
    """
    returns the number of subscribers on a subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print('None')
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    res = requests.get(url, params=params)
    data = res.json()

    try:
        hot_list = data.get('data').get('children')
        for item in hot_list:
            print(item.get('data').get('title'))
    except Exception:
        print('None')
