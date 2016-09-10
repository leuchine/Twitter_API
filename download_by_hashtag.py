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

text=[]
flag=True 

hashtag='#travel'
num=2000
while flag:
    try:
        #q='keywords' or '#hashtag'
        for tweet in tweepy.Cursor(api.search, q=hashtag).items(num):
            text.append(tweet.text.lower())
            print(len(text))
        flag=False
    except tweepy.TweepError,e:
        print(str(e))
        setToken()

reload(sys)
sys.setdefaultencoding("utf-8")
fileObj = codecs.open("travel.csv", "w", encoding="utf-8")
for i in text:
    fileObj.write(str(i.lower().replace(hashtag,'').replace('\n',''))+";;"+str('pos')+"\n")
fileObj.close()