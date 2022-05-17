#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


def request_rest_api(user_id):
    """ make request to the API """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users?id={}".format(url, user_id)).json()[0]
    u_name = user.get("name")
    print("Employee {} is done with tasks".format(u_name), end='')
    tasks = requests.get("{}todos?userId={}".format(url, user_id)).json()
    done = 0
    for rev in tasks:
        if rev.get('completed'):
            done = done + 1
    print("({}/{}):".format(done, len(tasks)))
    for rev in tasks:
        if rev.get('completed'):
            print("\t {}".format(rev.get('title')))


if __name__ == '__main__':
    request_rest_api(argv[1])
