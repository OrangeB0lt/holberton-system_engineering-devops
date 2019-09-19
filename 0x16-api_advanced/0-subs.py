#!/usr/bin/python3
''' queries to https://www.reddit.com/dev/api/ '''
import requests


def number_of_subscribers(subreddit):
    ''' returns the num of subscribers '''
    domain = 'https://www.reddit.com'
    path = '/r/{}/about.json'.format(subreddit)
    fullurl = '{}{}'.format(domain, path)
    header = {
        'user-agent': 'Holby_The_Human_Boy',
        'over18': 'yes'
    }
    response = requests.get(
        fullurl,
        headers=header,
        allow_redirects=False
    )
    code = response.status_code
    if code >= 300:
        return 0
    data = response.json().get('data')
    subscribers = data.get('subscribers')
    return subscribers
