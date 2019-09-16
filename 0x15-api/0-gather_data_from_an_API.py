#!/usr/bin/python3
'''
Uses https://jsonplaceholder.typicode.com/ REST API, for a given
employee ID, returns info on their TODO list prog
'''
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

    doneTasks = []
    totalTasks = len(todoDictList)
    employee = userDictList[0].get('name')

    for task in todoDictList:
        if task.get('completed') is True:
            doneTasks.append(task)

     print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(doneTasks), totalTasks))

     for task in doneTasks:
        print("\t {}".format(task.get('title')))
