import tweepy
import os
#override tweepy.StreamListener to add logic to on_status

consumer_key = '8YafE9PzHuzH4kita1dvPIA03'
consumer_secret = 'CyEW2E3bXeisaFeKzQ9DWuZ2PasHwAgSLx5w7lbUTypg8wtazo'
access_token = '4746024492-phNkGNoTfLYir0tN2zeYwIr9mAOOP0INprGjD19'
access_token_secret = 'beBttOOTaFqGjWkpFFmf8EecB8IO3kPG8y3iRqzPFWQsG'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        entity = status.entities['hashtags']




        if(len(entity)>0):
            text = entity[0]['text']
            if(text == 'coronavirus' or text == 'Coronavirus' or text == 'CoronaVirus' or text == 'COVID' or text == 'COVID-19'):
                #print('SUCESS') DEBUG
                username = status.user.name
                times = status.created_at
                location = status.user.location
                language = status.lang

                fileHandler = open('name3.txt', 'r+')
                while True:
                    line = fileHandler.readline()
                    if line.strip() == (username + ' / ' + str(times)):
                        break
                    if not line:
                        fileHandler.write(username + ' / ' + str(times) + '\n')



                        f = open('location.txt', 'r+')
                        while True:
                            line2 = f.readline()
                            if not line2:
                                f.write(str(location))
                                f.write('\n')
                                break

                        languageFile = open('language.txt', 'r+')
                        while True:
                            line3 = languageFile.readline()
                            if not line3:
                                languageFile.write(str(language)+'\n')
                                break
                        languageFile.close()             
                        break

                    #print(line.strip())
                fileHandler.close()

                #print(username, times)
        #print(status.entities['hashtags'])
    

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, myStreamListener)
myStream.filter(track=['coronavirus', 'CoronaVirus', 'COVID', 'COVID-19'])