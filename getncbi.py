import os

lines = []

with open('projlist2.txt') as f:
    lines = f.read().splitlines()

count = 0
for line in lines:
    count += 1
    print("Project {}: {}".format(count,line)) 
    query = "esearch -db sra -query '{}[bioproject]' | efetch -format runinfo | cat > {}.csv".format(line,line)
    os.system(query) 
    print("DONE") 


