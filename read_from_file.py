# coding: utf-8

tweets=[]
with open('sample.csv') as f:
    for line in f:
        tweets+=[line.split('\t')]

for i in tweets:
    print(i)

### text mining to be done