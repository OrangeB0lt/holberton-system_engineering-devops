#!/usr/bin/python3
"""
Pings a To-Do API for data for all users and writes it to a JSON file
"""
import csv
import json
import requests


if __name__ == '__main__':
    employee_id = 1
    userTasks = {}
    urlTodo = 'https://jsonplaceholder.typicode.com/todos/'
    urlUser = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(urlUser).json()

    for employee_id in range(1, len(users) + 1):
        todo = requests.get(urlTodo, params={'userId': employee_id})
        user = requests.get(urlUser, params={'id': employee_id})

        todoDictList = todo.json()
        userDictList = user.json()
        taskList = []
        employee = userDictList[0].get('username')

        for task in todoDictList:
            status = task.get('completed')
            title = task.get('title')
            taskDict = {}
            taskDict['task'] = title
            taskDict['completed'] = status
            taskDict['username'] = employee
            taskList.append(taskDict)
        userTasks[employee_id] = taskList

    with open("todo_all_employees.json", "w+") as jsonfile:
        json.dump(userTasks, jsonfile)
