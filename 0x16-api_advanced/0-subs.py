#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ function to get number of suscribers """
    if not subreddit:
        return 0
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "j4ir0st"}
    sub = "{}{}/about.json".format(url, subreddit)
    req = requests.get(sub, headers=headers, allow_redirects=False).json()
    subs = req.get("data", {}).get("subscribers", 0)
    return subs
