import sys
import fileinput


def main(separator='\t'):
        word_id_lst = []
        for line in fileinput.input():
            line = line.rstrip()
            #print(line)
            line = line.split('\t')
            #print(line)
            word_id_lst.append(line)
        
        #print(word_id_lst)
        d = {}
        for element in word_id_lst:
            if element[0] not in d:
               d[element[0]] = 1
            else:
               #print(element[1)]
               d[element[0]] = d[element[0]]+1
        #print(d['anyone '])
        #print(d['eBook '])
        #print(d)
        sorted_ngram = sorted(d.items(),key = lambda x:-x[1])[:10]
        for element in sorted_ngram:
            print("{0}\t{1}".format(*element))
        '''for key, value in d.items():
            print(key + separator + str(value))'''


            
        
            
        

if __name__ == "__main__":
	main()

