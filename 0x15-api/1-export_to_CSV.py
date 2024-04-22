#!/usr/bin/python3
"""
This script fetches the user's data and TODO list, and then exports them to a CSV file named USER_ID.csv.
"""

import requests
import sys


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/"

    response = requests.get(url)
    username = response.json().get("username")

    response = requests.get(url + "todos")
    employee_todos = response.json()

    with open(f'{sys.argv[1]}.csv', 'w') as file:
        for task in employee_todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(sys.argv[1], username,
                               task.get('completed'),
                               task.get('title')))
