#!/usr/bin/python3
import pandas as pd
import os

lines = []

with open('projlist.txt') as f:
    lines = f.read().splitlines()

count = 0
acclist = []
for line in lines:
    count += 1
    print ("Project {}: {}".format(count,line))
    my_csv = pd.read_csv("./bioproject/{}".format(line))
    column = my_csv['Run'].to_list()
    acclist.extend(column)
    #print(column)
print("acc",len(acclist))

acclist = list(set(acclist)) #removes duplicates
print("acc",len(acclist))
df = pd.DataFrame(acclist)
print(True in df.duplicated().to_list())
df.to_csv('acclist.csv',index=False)




