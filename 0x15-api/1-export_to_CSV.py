#!/usr/bin/python3
'''Module with script to use REST API to track employee ID
and return todo list export in csv format'''

import csv
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    to_dos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        emp_id)
    user_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    todo_resp = requests.get(to_dos)
    user_resp = requests.get(user_name).json()
    emp_name = user_resp['name']
    u_name = user_resp['username']
    tc = 0
    chk = 0
    task_list = []
    the_file = "{}.csv".format(emp_id)

    for data in todo_resp.json():
        done = data['completed']
        task = data['title']
        with open(the_file, mode='a') as csv_file:
            emp_tasks = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            emp_tasks.writerow([emp_id, u_name, done, task])
