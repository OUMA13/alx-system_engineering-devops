#!/usr/bin/python3

"""
queries the Reddit API
"""

from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version  120.0.6099.199'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        data = results.get('data').get('children')

        for i in data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
