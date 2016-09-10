# coding: utf-8
import tweepy
import random
import codecs
import time
import csv
import sys

def setToken():
    global consumer_key
    global access_token
    global access_token_secret
    global consumer_secret
    global tokens_list
    global auth
    global api
    index = random.randint(0, len(tokens_list)-1)
    
    print(tokens_list[index])
    consumer_key=tokens_list[index][1]
    consumer_secret=tokens_list[index][2]
    access_token=tokens_list[index][3]
    access_token_secret=tokens_list[index][4]
    

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


tokens_list = []
with open('tokens.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        tokens_list.append(row)

consumer_key = None
access_token = None
access_token_secret = None
consumer_secret=None
auth=None
api=None
setToken()

usernum=70
randuser =  [[0 for j in range(100)] for i in range(usernum)]

i=0
while i<usernum:
    #generate random user number
    randuser[i][0] = random.randrange(10,100000000)
    try:
        #get user name
        randuser[i][1] = api.get_user(randuser[i][0]).name
        print(randuser[i][1])

        #get user timeline status
        text=[]
        for tweet in tweepy.Cursor(api.user_timeline,id=randuser[i][0]).items():
            text.append(tweet.text)
        randuser[i][2] = text
    except tweepy.TweepError,e:
        print(str(e))
        if '429' in str(e) or '89' in str(e): 
            setToken()
        i-=1
    i+=1

reload(sys)
sys.setdefaultencoding("utf-8")
fileObj = codecs.open("sample.csv", "w", encoding="utf-8")
for i in randuser:
    for j in i[2]:
        j=j.replace('\n',' ')
        fileObj.write(str(i[0])+"\t"+str(i[1])+"\t"+str(j)+"\n")
