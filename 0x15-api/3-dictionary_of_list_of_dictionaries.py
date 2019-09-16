#!/usr/bin/python3
'''
Pings a To-Do API for data for all users and writes it to a JSON file
'''
if __name__ == "__main__":
    import json
    import requests
    import sys
    rootURL = 'https://jsonplaceholder.typicode.com/'

    # grab info about all users
    url = rootURL + 'users'
    response = requests.get(url)
    users = json.loads(response.text)

    # grab the info about the users' tasks
    constructor = {}
    for user in users:
        employee_id = user.get('id')
        user_id_key = str(employee_id)
        username = user.get('username')
        constructor[user_id_key] = []
        url = rootURL + 'todos?userId={}'.format(employee_id)

        response = requests.get(url)
        objs = json.loads(response.text)
        for obj in objs:
                json_data = {
                    "username": username
                    "task": obj.get('title'),
                    "completed": obj.get('completed'),
                }
                constructor[user_id_key].append(json_data)

    # write the data to the file
    json_encoded_data = json.dumps(constructor)
    with open('todo_all_employees.json', 'w') as myFile:
        myFile.write(json_encoded_data)