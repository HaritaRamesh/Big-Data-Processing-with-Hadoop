import sys
import os
import nltk

def main(separator='\t'):
        filepath = os.environ["map_input_file"]
        filename = os.path.split(filepath)[-1]
        #data = read_input(sys.stdin)
        for line in sys.stdin:
            line = line.lower()
            line = line.replace('"','')
            line = line.replace('.','')
            line = line.replace(',','')
            line = line.replace('!','')
            line = line.replace(':','')
            line = line.replace("'",'')
            line = line.replace("_",'')
            line = line.replace(";",'')
            line = line.replace("(","")
            line = line.replace(")","")
            line = line.rstrip()
            tokenizer = nltk.RegexpTokenizer(r"\w+")
            words = tokenizer.tokenize(line)
            #print(words)
            for word in words:
                print(word, separator, filename)
            #Mapper output
            #word1	filename1
            #word2	filename2

if __name__ == "__main__":
	main()

