#!/usr/bin/python3
""" queries the Reddit API """

from requests import get


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given, the function
    should return 0.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version  120.0.6099.199'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
