#!/usr/bin/python3
import pandas as pd
import os

lines = []
def remove_items(test_list, item):    
    # using list comprehension
    res = [i for i in test_list if i != item]
    return res 

with open('projlist.txt') as f:
    lines = f.read().splitlines()

tcount = 0
counter = 0 
acclist = []
for line in lines:
    counter += 1
    my_csv = pd.read_csv("./bioproject/{}".format(line))
    column = my_csv['Run'].to_list()
    #print(column)
    column = remove_items(column,'Run')
    column = remove_items(column,0)
    count = len(column)
    tcount +=count
    with open('srasinproj.txt','a') as w:
    	w.write("Project {}: {} Runs: {} \n".format(counter,line,count))
    print ("Project {}: {} Runs: {}".format(count,line,count))
    df = pd.DataFrame(column)
    df.to_csv("./sra/{}.csv".format(line),index=False,header=False) 
    
print("Total Runs:",tcount)
with open('srasinproj.txt','a') as w:
	w.write("Total Runs:{} \n".format(tcount))

