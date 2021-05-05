#!/usr/bin/python3
'''Module with script to use REST API to track employee ID
and return todo list  export data in the JSON format'''

import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_name = 'https://jsonplaceholder.typicode.com/users/'
    user_resp = requests.get(user_name).json()
    user_id_list = []

    for emps in user_resp:
        emp_name = emps.get("name")
        u_name = emps.get("username")
        user_id = emps.get("id")
        user_id_list.append(user_id)
        final_dict = {}
        final_dict[user_id] = []

        for employee in user_id_list:
            the_file = "todo_all_employees.json"
            to_dos = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
                .format(user_id)
            todo_resp = requests.get(to_dos)

            for data in todo_resp.json():
                task = data["title"]
                done = data["completed"]
                task_dict = {
                    "task": task, "completed": done, "username": u_name
                }
                final_dict.get(user_id).append(task_dict)

                with open(the_file, mode='w') as json_file:
                    j_str = json.dumps(final_dict)
                    json_file.write(j_str)
