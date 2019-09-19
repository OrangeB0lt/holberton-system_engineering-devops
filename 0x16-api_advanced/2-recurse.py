#!/usr/bin/python3
''' queries to https://www.reddit.com/dev/api/ '''
import requests


def getRequest(subreddit, after, hot_list):
    ''' creates get request to reddit API '''
    fullurl = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        payload = {
            'after': after, 'count': str(len(hot_list)), 'limit': '100'
        }
    else:
        payload = {'limit': '100'}
    header = {
        'user-agent': 'Holby_The_Human_Boy',
        'over18': 'yes'
    }
    response = requests.get(
        fullurl, headers=header,
        params=payload, allow_redirects=False
    )
    return response


def titles(hot_list, child):
    """
    adds new titles to hottlist
    """
    for kid in child:
        hot_post = kid.get('data')
        title = hot_post.get('title')
        hot_list.append(title)
    return hot_list


def recurse(subreddit, hot_list=[], after=None):
    ''' returns the top ten hot posts for subreddit '''
    response = getRequest(subreddit, after, hot_list)
    statcode = response.status_code
    if statcode >= 300:
        return None
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    hot_list = titles(hot_list, children)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
