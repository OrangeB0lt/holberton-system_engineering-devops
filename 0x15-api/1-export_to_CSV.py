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

    # grab info abt the user
    url = rootURL + 'users?id={}'.format(employee_id)
    response = requests.get(url)
    user = json.loads(response.text)
    user_name = user[0].get('username')

    # grab info abt the user's tasks
    url = rootURL + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    constructor = ""
    for obj in objs:
            constructor += '"{}","{}","{}","{}"\n'.format(
                employee_id,
                user_name,
                obj.get('completed'),
                obj.get('title')
            )
    with open('{}.csv'.format(employee_id), 'w') as myFile:
        myFile.write(constructor)