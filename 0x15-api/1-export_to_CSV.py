#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
import json
import requests
from sys import argv


def request_rest_api(user_id):
    """ make request to the API """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users?id={}".format(url, user_id)).json()[0]
    tasks = requests.get("{}todos?userId={}".format(url, user_id)).json()
    lst = []
    for rev in tasks:
        lst.append([user_id, user['username'], rev['completed'], rev['title']])
    file_name = '{}.csv'.format(user_id)
    with open(file_name, mode='w') as fd:
        w = csv.writer(fd, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in lst:
            w.writerow(row)


if __name__ == '__main__':
    request_rest_api(argv[1])
