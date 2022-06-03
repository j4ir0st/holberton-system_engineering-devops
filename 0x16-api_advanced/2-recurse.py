#!/usr/bin/python3
"""
Recursive Function that queries the Reddit API and
returns the titles of the all hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ function to get number of suscribers """
    url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "j4ir0st"}
    par = {"after": after}
    sub = "{}{}/hot.json".format(url, subreddit)
    req = requests.get(sub, headers=headers, params=par, allow_redirects=False)
    if after is None:
        return hot_list
    if req.status_code == 200:
        hot = req.json()
        after = hot.get("data").get("after")
        hots = hot.get("data").get("children")
        hot_list += list(map(lambda elm: elm.get("data").get("title"), hots))
        return recurse(subreddit, hot_list, after)
    else:
        return None
