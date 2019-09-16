#!/usr/bin/python3
'''
Uses https://jsonplaceholder.typicode.com/ REST API, for a given
employee ID, returns info on their TODO list prog
'''
import requests
import sys



def makeRequest(data, num):
    ''' makes employee request and returns json dict response '''
    rootURL = 'https://jsonplaceholder.typicode.com'
    url = '{}{}{}'.format(rootURL, data, num)
    return requests.get(url).json()


def application(num):
    ''' makes request for info about employee todo list, then prints '''
    employee = makeRequest('/users/', num)
    todos = makeRequest('/todos/?userId=', num)
    completed = [i.get('title') for i in todos if i.get('completed')]
    total = len(todos)
    print('Employee {} is done with tasks({}/{}):'.format(
        employee.get('name'), len(completed), total))
    for i in completed:
        print('\t {}'.format(i))


if __name__ == '__main__':
    """
    MAIN App
    """
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        application(sys.argv[1])
