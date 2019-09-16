#!/usr/bin/python3
'''
Pings a To-Do API for data for a specified user and writes it to a JSON file
'''
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    urlTodo = 'https://jsonplaceholder.typicode.com/todos/'
    urlUser = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(urlTodo, params={'userId': employee_id})
    user = requests.get(urlUser, params={'id': employee_id})

    todoDictList = todo.json()
    userDictList = user.json()
    taskList = []
    userTasks = {}
    employee = user_dict_list[0].get('username')

    with open("{}.json".format(employee_id), "w+") as jsonfile:
        for task in todoDictList:
            status = task.get('completed')
            title = task.get('title')
            taskDict = {}
            taskDict['task'] = title
            taskDict['completed'] = status
            taskDict['username'] = employee
            taskList.append(taskDict)
        userTasks[employee_id] = taskList

        data = json.dumps(userTasks)
        jsonfile.write(data)
