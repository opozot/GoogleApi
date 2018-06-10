from __future__ import print_function

from apiclient import discovery

TMPL = '''
    User: %s
    Date: %s
    Post: %s
'''

API_KEY = 'AIzaSyCI-nUTyNwS9XzgksA97cZT9KxZl6K8aR0'
GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)
items = GPLUS.activities().search(query='python').execute().get('items', [])
for data in items:
    post = ' '.join(data['title'].strip().split())
    if post:
        print(TMPL % (data['actor']['displayName'], data['published'], post))
