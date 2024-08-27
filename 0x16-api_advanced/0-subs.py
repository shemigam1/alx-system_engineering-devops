#!/usr/bin/python3

"""
this script queries the reddit api 
for the number of subscribers on a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    returns the number of subscribers on a subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url)
    data = res.json()

    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0
