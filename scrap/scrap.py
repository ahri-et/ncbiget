from bs4 import BeautifulSoup
import requests,re
import xml.etree.ElementTree as ET



def getbiosamlist4proj(prj_acc):
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

	url2 = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=bioproject&db=biosample&id={}&linkname=bioproject_biosample_all&cmd=neighbor_history".format(uid)

	req2 = requests.get(url2)
	#soup2 = BeautifulSoup(req2.text,"html.parser")
	#print(req2.text)
	root = ET.fromstring(req2.text)
	webenv= root[0][3].text
	querykey=root[0][2][2].text
	#print(type(root))
	print(querykey,webenv)

	biosam_count = nums[1]
	print("Fetching {}.txt".format(prj_acc))
	url3 = "https://www.ncbi.nlm.nih.gov/portal/utils/file_backend.cgi?Db=biosample&HistoryId={}&QueryKey={}&Sort=&Filter=all&CompleteResultCount={}&Mode=file&View=acclist&p$l=Email&portalSnapshot=/projects/BioSample/biosample@1.36&BaseUrl=&PortName=live&FileName=".format(webenv,querykey,biosam_count)
	req3 = requests.get(url3)
	
	with open("{}.txt".format(prj_acc),"w") as f:
		f.write(req3.text)
	print("DONE {}.txt".format(prj_acc))

if __name__ == "__main__":

	lines = []

	with open("../projlist.txt","r") as reader:
		lines = reader.read().splitlines()

	count = 0
	for line in lines:
		count += 1
		print("#######{}".format(count))
		getbiosamlist4proj(line)
