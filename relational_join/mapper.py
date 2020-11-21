#!/usr/bin/env python
import pandas as pd
import sys
data1 = sys.stdin.read().splitlines()
for l in data1:
    l = l.split(",")
    #print(l)
    # The data from the two csv files are differentiated using the no. of columns in this example. A key is added to ensure the data from all the mappers goes to the same reducer.
    if len(l) == 2:
        print('1' + '\t:' + l[0] + ':' + l[1])
    elif len(l) == 5:
        temp1 = l[0]
        temp2 = l[1] + ',' + l[2]
        temp3 = l[3]
        temp4 = l[4]
        print('1' + '\t:' + temp1 + ':' + temp2.strip("\"") + ':' + temp3.strip("\"") + ':' + temp4)
    else:
        temp1 = l[0] 
        temp2 = l[1] + ',' + l[2] 
        temp3 = ','.join(l[3:len(l) - 1])
        temp4 =  l[len(l) - 1]
        print('1' + '\t:' + temp1 + ":" + temp2.strip("\"") + ":" + temp3.strip("\"") + ":" + temp4)
   
