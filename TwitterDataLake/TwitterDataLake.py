import TwitterAPI
import json

consumer_key = 'BiBXPCGSIxaH3IUc98H7SfRgs'
consumer_secret = 'eig9biZmFBVK8iy1VobOwwIsvaD7jM6fF0ODmUulc8yTJVpaCZ'

filename = 'twitter_output.txt'
file = open(filename, 'a')

api = TwitterAPI.TwitterAPI(consumer_key=consumer_key, consumer_secret=consumer_secret, auth_type='oAuth2')


pager = TwitterAPI.TwitterRestPager(api, 'statuses/user_timeline', {'count':200, 'screen_name':'wx_copenhagen'})

def process_tweet(file, tweet):
    file.write(tweet + '\n')

i = 0
last_id = 0
for item in pager.get_iterator(wait=1):
    if 'text' in item:
        process_tweet(file, item['text'])
        last_id = item['id']
        print(item['text'])
    elif (('message' in item) and ('message' != 200)):
        break
    i += 1
    if i > 38000:
        break
print(i)

file.close()