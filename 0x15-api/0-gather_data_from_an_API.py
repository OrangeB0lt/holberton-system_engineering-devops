#!/usr/bin/python3
'''
script for parsing web data from an api
'''
if __name__ == "__main__":
    import json
    import requests
    import sys
    rootURL = 'https://jsonplaceholder.typicode.com/'
    try:
        employee_id = sys.argv[1]
    except:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        exit(1)

    # grab user info
    url = rootURL + 'users?id={}'.format(employee_id)
    response = requests.get(url)
    user = json.loads(response.text)
    name = user[0].get('name')

    # grab user's tasks info
    url = rootURL + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    completed = 0
    compTasks = []
    for obj in objs:
        if obj.get('completed'):
            compTasks.append(obj)
            completed += 1

    # print output user's task completion
    print("Employee {} is done with tasks({}/{}):".format(name, completed, len(objs)))
    # print output title of completed tasks
    for task in compTasks:
        print("\t {}".format(task.get('title')))