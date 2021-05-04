#!/usr/bin/python3
'''Module with script to use REST API to track employee ID
and return todo list'''

import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    to_dos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        emp_id)
    user_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    todo_resp = requests.get(to_dos)
    user_resp = requests.get(user_name).json()
    emp_name = user_resp['name']
    tc = 0
    chk = 0
    task_list = []

    """
    todo_resp.json()[0]----> {'userId': 2, 'completed': False, 'title':
    'suscipit repellat esse quibusdam voluptatem incidunt', 'id': 21}
    """
    for data in todo_resp.json():
        done = data['completed']
        task = data['title']
        tc = tc + 1
        if done:
            task_list.append(task)
            chk = chk + 1
    print("Employee {} is done with tasks({}/{}):".format(emp_name, chk, tc))

    for task in task_list:
        print("\t {}".format(task))
