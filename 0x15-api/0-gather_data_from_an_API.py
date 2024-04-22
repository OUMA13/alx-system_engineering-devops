#!/usr/bin/python3
"""
return to do list information for a given employee ID
"""

import requests
import sys


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/"

    response = requests.get(url)
    employee_name = response.json().get("name")

    response = requests.get(url + "todos")
    employee_todos = response.json()

    completed_tasks = [
        task for task in employee_todos if task.get('completed')]
    completed = len(completed_tasks)
    total = len(employee_todos)

    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    [print(f"\t {task.get('title')}") for task in completed_tasks]
