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
    emp_id_list = []
    for emps in user_resp:
        emp_name = emps.get('name')
        u_name = emps.get('username')
        emp_id = emps.get('id')
        emp_id_list.append(emp_id)

        for employee in emp_id_list:
            emp_id = employee
            dict_list = []
            final_list = []
            the_file = "todo_all_employees.json"
            final_dict = {}
            to_dos = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
                .format(emp_id)
            todo_resp = requests.get(to_dos)
            for data in todo_resp.json():
                task = data['title']
                done = data['completed']
                task_dict = {
                    "task": task, "completed": done, "username": u_name
                }
                dict_list.append(task_dict)
                final_dict[emp_id] = dict_list

                with open(the_file, mode='a') as json_file:
                    j_str = json.dump(final_dict)
                    json_file.write(j_str)
