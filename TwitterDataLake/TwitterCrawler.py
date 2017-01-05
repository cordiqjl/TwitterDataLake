import TwitterAPI
import json
import os

consumer_key = 'BiBXPCGSIxaH3IUc98H7SfRgs'
consumer_secret = 'eig9biZmFBVK8iy1VobOwwIsvaD7jM6fF0ODmUulc8yTJVpaCZ'

filename = 'twitter_output.txt'
file = open(filename, 'a')

filename_id = 'since_id.txt'
file_id = open(filename_id, 'r')
if os.stat(filename_id).st_size == 0:
    since_id = ''
else:
    ids = file_id.readlines()
    since_id = ids[-1]
file_id.close()

api = TwitterAPI.TwitterAPI(consumer_key=consumer_key, consumer_secret=consumer_secret, auth_type='oAuth2')

if since_id:
    pager = TwitterAPI.TwitterRestPager(api, 'statuses/user_timeline', {'count':200, 'screen_name':'wx_copenhagen', 'since_id':since_id})
else:
    pager = TwitterAPI.TwitterRestPager(api, 'statuses/user_timeline', {'count':200, 'screen_name':'wx_copenhagen'})

def process_tweet(file, tweet):
    file.write(tweet + '\n')

i = 0
last_id = 0
for item in pager.get_iterator(wait=1):
    if 'text' in item:
        process_tweet(file, item['text'])
        if i == 0:
            last_id = item['id']
        if last_id < item['id']:
            last_id = item['id']
        print(item['text'])
    elif (('message' in item) and ('message' != 200)):
        break
    i += 1
    if i > 38000:
        break
print(i)

file.close()

file_id = open(filename_id, 'a')
file_id.write(str(last_id) + '\n')
file_id.close()