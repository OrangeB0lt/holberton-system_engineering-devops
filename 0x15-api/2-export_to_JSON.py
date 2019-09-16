#!/usr/bin/python3
'''
Pings a To-Do API for data for a specified user and writes it to a JSON file
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

    # grab the info about the user
    url = rootURL + 'users?id={}'.format(employee_id)
    response = requests.get(url)
    user = json.loads(response.text)
    userName = user[0].get('username')

    # grab the info about the user's tasks
    url = rootURL + 'todos?userId={}'.format(employee_id)
    response = requests.get(url)
    objs = json.loads(response.text)
    user_id_key = str(employee_id)
    constructor = {user_id_key: []}
    for obj in objs:
            json_data = {
                "task": obj.get('title'),
                "completed": obj.get('completed'),
                "username": userName
            }
            constructor[user_id_key].append(json_data)
    json_encoded_data = json.dumps(constructor)
    with open('{}.json'.format(employee_id), 'w') as myFile:
        myFile.write(json_encoded_data)