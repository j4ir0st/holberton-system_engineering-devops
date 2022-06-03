#!/usr/bin/python3
"""
Recursive Function that queries the Reddit API and
returns the titles of the all hot posts
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ function to get number of suscribers """
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "j4ir0st"}
    sub = "{}{}/hot.json?".format(url, subreddit)
    req = requests.get(sub, headers=headers, allow_redirects=False).json()
    hot = req.get("data", {}).get("children", None)
    for data in hot:
        title = data.get("data").get("title")
        return("{}".format(title))
