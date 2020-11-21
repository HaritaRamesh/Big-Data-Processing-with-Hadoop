from itertools import groupby
from operator import itemgetter
import sys
import fileinput

def main(separator='\t'):
       #Splitting the mapper output by tab
        word_id_lst = []
        for line in fileinput.input():
            line = line.rstrip()
            line = line.split('\t')
            word_id_lst.append(line)
        
        #Accumulating the words and txt files
        d = {}
        for element in word_id_lst:
            if element[0] not in d:
               d[element[0]] = []
               d[element[0]].append(element[1])
            else:
               if element[1] not in d[element[0]]:
                  d[element[0]].append(element[1])

        for key, value in d.items():
            print(key,separator,str(value))

        #Reducer output
        #word1	["filename1","filename2"]
        #word3	["filename3]

if __name__ == "__main__":
	main()

