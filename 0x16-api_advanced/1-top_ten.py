#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """ function to get number of suscribers """
    if not subreddit:
        return 0
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "j4ir0st"}
    sub = "{}{}/hot.json?limit=10".format(url, subreddit)
    req = requests.get(sub, headers=headers, allow_redirects=False).json()
    hot = req.get("data", {}).get("children", 0)
    for data in hot:
        title = data.get("data").get("title")
        print("{}".format(title))
