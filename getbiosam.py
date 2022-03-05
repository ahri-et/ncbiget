import os
import sys

def remove_items(test_list,item):
    res = [i for i in test_list if i!= item]
    return res

def fetch_biosam(startprojn,startbiosamn):
    projects = []
    with open('projlist.txt') as f:
        projects = f.read().splitlines()

    pcount = 0
    for project in projects:
        pcount += 1
        if pcount < startprojn: 
            continue
        print("~~~Project {}: {} ~~~".format(pcount,project)) 
        biosamples = []
        with open('./biosample/{}.txt'.format(project)) as p:
            biosamples = p.read().splitlines()
        biosamples = remove_items(biosamples,'')
        bcount = 0
        for biosample in biosamples:
            bcount += 1
            if (pcount == startprojn) and (bcount < startbiosamn):
                continue     
            print("Biosample {}: {}".format(bcount,biosample)) 
            os.system("esearch -db biosample -query '{}' | efetch -format xml | cat > ./biosample/{}/{}.xml".format(biosample,project,biosample)) 
        #print(biosamples)
        print("DONE") 


if __name__ == '__main__':
    
    fetch_biosam(int(sys.argv[1]),int(sys.argv[2]))


