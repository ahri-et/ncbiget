from bs4 import BeautifulSoup
import requests,re
import pandas as pd
import numpy as np


def getmeta4proj(prj_acc):
	print("~~~~~~{}~~~~~".format(prj_acc))
	url = "https://www.ncbi.nlm.nih.gov/bioproject/?term={}".format(prj_acc)
	req = requests.get(url)
	soup = BeautifulSoup(req.text,"html.parser")

	res = [] 	#list to be populated by biosample and sra link
	nums = []
	for link in soup.find_all('a'):
		if link.get('id') == 'BioSample' or  link.get('id') == 'SRA Experiments': 
			#print(link.string,link.get('id'),link.get('href'))
			nums.append(link.string)
			res.append(link.get('href'))
			#print(link)

	uid = re.findall(r'(?<=from_uid\=)\d+',res[0])[0]
	print(nums)
	print(uid)
	nums.append(uid)
	return nums

if __name__ == "__main__":

	lines = []
	with open("../projlist.txt","r") as f:
		lines=f.read().splitlines()

	df = pd.DataFrame(columns=['BioProject','SRA','BioSample','uid'])
	for line in lines:
		res = []
		meta = getmeta4proj(line)
		meta.insert(0,line)
		res.insert(0,meta)
		df = df.append(pd.DataFrame(res,columns=['BioProject','SRA','BioSample','uid']),ignore_index=True)
		print(df)
	df.index = np.arange(1, len(df)+1) #set index to start from 1
	df.to_csv("ProjectMetaNum.csv")
