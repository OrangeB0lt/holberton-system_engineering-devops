#!/usr/bin/python3
''' queries to https://www.reddit.com/dev/api/ '''
import requests


def top_ten(subreddit):
    ''' returns the top 10 posts '''
    domain = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
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
    statCode = response.status_code
    if statCode >= 300:
        print('None')
    else:
        info = response.json().get('data')
        child = info.get('children')
        for kid in range(10):
            hotPost = child[kid].get('data')
            tTitle = hotPost.get('title')
            print('{}'.format(tTitle))
