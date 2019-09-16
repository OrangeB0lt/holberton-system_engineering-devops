#!/usr/bin/python3
'''
Pings To-Do API for data on specified user and saves the data to a CSV file
'''
import csv
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

    employee = userDictList[0].get('username')

    with open("{}.csv".format(employee_id), "a+") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todoDictList:
            status = task['completed']
            title = task['title']
            csvwriter.writerow(["{}".format(employee_id),
                                "{}".format(employee),
                                "{}".format(status),
                                "{}".format(title)])
