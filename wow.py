import tweepy
import json
import os
import time
import sys
consumer_key = '8YafE9PzHuzH4kita1dvPIA03'
consumer_secret = 'CyEW2E3bXeisaFeKzQ9DWuZ2PasHwAgSLx5w7lbUTypg8wtazo'
access_token = '4746024492-phNkGNoTfLYir0tN2zeYwIr9mAOOP0INprGjD19'
access_token_secret = 'beBttOOTaFqGjWkpFFmf8EecB8IO3kPG8y3iRqzPFWQsG'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#, parser=tweepy.parsers.JSONParser()

# search = api.search('asdfghjkl')

# for tweet in search:
#     print(tweet.text, tweet.created_at, '\n\n\n')





# query = 'coronavirus'                         search using cursor
# print('hi')
# max_tweets = 10
# searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
# for tweet in searched_tweets:
#     print(tweet.user.name,'\n\n\n\n\n')


public_tweets = api.search('Coronavirus')

# # json.dumps(public_tweets)
# while(True):
#     public_tweets = api.search('Coronavirus')
#     for tweet in public_tweets:
#         entity = tweet.entities['hashtags']
#         if(len(entity)>0):
#             text = entity[0]['text']
#             if(text == 'coronavirus' or text == 'Coronavirus'):
#                 #print('SUCESS') DEBUG
#                 username = tweet.user.name
#                 times = tweet.created_at

#                 # fileHandler = open('Desktop/wow.txt', 'r+')
#                 # while True:
#                 #     line = fileHandler.readline()
#                 #     if line.strip() == (username + ' / ' + str(times)):
#                 #         break;
#                 #     if not line:
#                 #         fileHandler.write(username + ' / ' + str(times) + '\n')
#                 #         break;
#                 #     #print(line.strip())
#                 # fileHandler.close()

#                 # print(username, times)

#             print(json.dumps(tweet._json, indent=2))     #PRETTY JSON
#             #print(text)
#     time.sleep(5)

    #print(entity)
    #json = json.loads(tweet._json)
    #value = json['entities']
    
    #hashtag = tweet._json.entities.hashtags
    #print(hashtag)
    
#print(public_tweets._json., '--------------------------------------------------------------------------------------\n\n\n')
for tweet in public_tweets:

     print(tweet.user.location)