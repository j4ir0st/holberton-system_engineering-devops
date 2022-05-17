#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
import json
import requests
from sys import argv


def request_rest_api():
    """ make request to the API """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users".format(url)).json()[0]
    data = {}
    for l_user in user:
        user_id = user['id']
        tasks = requests.get("{}todos?userId={}".format(url, user_id)).json()
        lst = []
        for rev in tasks:
            lst.append({
                "username": user['username'],
                "task": rev['title'],
                "completed": rev['completed'],
            })
        data[str(user_id)] = lst
    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    request_rest_api()
