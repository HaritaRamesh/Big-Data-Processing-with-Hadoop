
#!/usr/bin/env python
import sys
import csv
from collections import defaultdict
#from operator import itemgetter

wordcount = defaultdict(list)
headers = []
for line in sys.stdin:
    line = line.strip()
    l = line.split("\t")
    l = l[1]
    l = l.split(':')
    
# The data from the mapper can be put into right positions if we identify the file it belongs to. They can be differentiated by the columns.
    if len(l) == 3:
         wordcount[l[1]].insert(0,l[2])
    else:
         wordcount[l[1]].insert(1,l[2])
         wordcount[l[1]].insert(2,l[3])
         wordcount[l[1]].insert(3,l[4])

#The result is written into a csv file.
if len(wordcount.keys()) > 0:
    with open('join3.csv', mode='w') as file:
        for word in wordcount.keys():
            writer = csv.writer(file)
            l = [word]
            for i in range(0,len(wordcount[word])):
                l.append(wordcount[word][i])
            writer.writerow(l)
