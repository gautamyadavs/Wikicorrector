import os
import bz2
import re


all = os.listdir("extracted/")
doc = '<doc'
f = open('index.txt','w')
flag = 1

for a in sorted(all)[:-1]:
    if a != '.DS_Store':
        all_files = os.listdir("extracted/"+a)
        with bz2.open("extracted/"+a+'/wiki_00.bz2', "rt") as bz_file:
            x = ''
            for line in bz_file:
                x = line
                break
            m = re.search(" +id=\"(.*?)\"", x)
            print(m.group(1))
        with bz2.open("extracted/"+a+'/wiki_99.bz2', "rt") as bz_file:
            x = ''
            y = ''
            for line in bz_file:
                if doc in line:
                    y = line
            n = re.search(" +id=\"(.*?)\"", y)
            #label, text = line.rstrip('\n').split('\t')
            #text_words = text.split(',')
            print(n.group(1))
        f.write(a+' '+m.group(1)+' '+n.group(1)+'\n')
all_files = os.listdir("extracted/"+sorted(all)[-1])
with bz2.open("extracted/"+sorted(all)[-1]+'/wiki_00.bz2', "rt") as bz_file:
    x = ''
    for line in bz_file:
        x = line
        break
    m = re.search(" +id=\"(.*?)\"", x)
    print(m.group(1))
al = os.listdir("extracted/"+sorted(all)[-1]+'/')
with bz2.open("extracted/"+sorted(all)[-1]+'/'+sorted(al)[-1], "rt") as bz_file:
    x = ''
    y = ''
    for line in bz_file:
        if doc in line:
            y = line
    n = re.search(" +id=\"(.*?)\"", y)
    #label, text = line.rstrip('\n').split('\t')
    #text_words = text.split(',')
    print(n.group(1))
f.write(sorted(all)[-1]+' '+m.group(1)+' '+n.group(1)+'\n')
f.close()

for a in sorted(all):
    if a != '.DS_Store':
        all_files = os.listdir("extracted/"+a)
        f = open('extracted/'+a+'/index.txt','w')
        for al in sorted(all_files):
            if al != '.DS_Store' and al != 'index.txt':
                with bz2.open("extracted/"+a+'/'+al, "rt") as bz_file:
                    x = ''
                    print("extracted/"+a+'/'+al)
                    for line in bz_file:
                        x = line
                        break
                    m = re.search(" +id=\"(.*?)\"", x)
                    f.write(al+' '+m.group(1)+'\n')
        f.close()
