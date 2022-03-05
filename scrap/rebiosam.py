import os,re

files = []
os.system("find ../biosample -maxdepth 3 -type f -empty | cat > emptyfetchs.txt")
with open("emptyfetchs.txt","r") as f:
	files = f.read().splitlines()
print(len(files))
#print(files[0].split('/'))
for file in files:
	l = file.split('/')
	project = l[2]
	biosample = l[3].split('.')[0]
	print(project,biosample)
	os.system("esearch -db biosample -query '{}' | efetch -format xml | cat > ../biosample/{}/{}.xml".format(biosample,project,biosample)) 
     
