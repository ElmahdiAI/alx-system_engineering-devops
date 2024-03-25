#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee.
"""

import requests
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/user/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    try:
        todo_result = requests.get(todo_url).json()
        name_result = requests.get(name_url).json()
    except requests.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)

    todo_num = len(todo_result)
    todo_complete = sum(1 for todo in todo_result if todo.get("completed"))
    name = name_result.get("name")
    print(f"Employee {name} has completed {todo_complete}/{todo_num} tasks:")
    for todo in todo_result:
        if todo.get("completed"):
            print("\t", todo.get("title"))
