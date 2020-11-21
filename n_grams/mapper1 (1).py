import sys
import re
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

def main(separator='\t'):
        list_of_ngrams = []
        lemmatizer = WordNetLemmatizer()
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
            line = line.replace("-","")
            line = line.rstrip()
            
    
            n_gram  = re.findall(r'[A-Za-z0-9\,\.\"\'\:]*\s[A-Za-z0-9\.\,\"\'\:]*\s[A-Za-z0-9]*science[A-Za-z0-9]*\s[A-Za-z0-9\,\.\"\'\:]*\s[A-Za-z0-9\.\,\"\'\:]*', line)
            n_gram3 = re.findall(r'[A-Za-z0-9\,\.\"\'\:]*\s[A-Za-z0-9\.\,\"\'\:]*\s[A-Za-z0-9]*fire[A-Za-z0-9]*\s[A-Za-z0-9\,\.\"\'\:]*\s[A-Za-z0-9\.\,\"\'\:]*', line)
            n_gram6 = re.findall(r'[A-Za-z0-9\,\.\"\'\:]*\s[A-Za-z0-9\.\,\"\'\:]*\s[A-Za-z0-9]*sea[A-Za-z0-9]*\s[A-Za-z0-9\,\.\"\'\:]*\s[A-Za-z0-9\.\,\"\'\:]*', line)
            #print(line)
            #if len(n_gram) > 1:
            #   print(n_gram)
            #if len(n_gram3) > 1:
            #   print(n_gram3)
            #if len(n_gram6) > 1:
            #   print(n_gram6)
            if n_gram != []:
               for line1 in n_gram:  
                   word_verify_science = re.findall(r'[A-Za-z0-9]*science[A-Za-z0-9]*',line1)
                   if lemmatizer.lemmatize(word_verify_science[0]) == 'science':
                      line1 = line1.replace(word_verify_science[0],"$")
                      line1 = line1.split()
                      for i in range(0,len(line1) - 2):
                          act_ngram = line1[i]+"_"+line1[i+1]+"_"+line1[i+2]
                          if '$' in act_ngram:
                              list_of_ngrams.append(act_ngram)


            if n_gram3 != []:
               for line4 in n_gram3:
                   word_verify_fire = re.findall(r'[A-Za-z0-9]*fire[A-Za-z0-9]*',line4)
                   if lemmatizer.lemmatize(word_verify_fire[0]) == 'fire':
                       line4 = line4.replace(word_verify_fire[0],"$")
                       line4 = line4.split()
                       for i in range(0,len(line4) - 2):
                          act_ngram3 = line4[i]+"_"+line4[i+1]+"_"+line4[i+2]
                          if '$' in act_ngram3:
                              list_of_ngrams.append(act_ngram3)

           
            if n_gram6 != []:
               for line7 in n_gram6:
                   word_verify_sea = re.findall(r'[A-Za-z0-9]*sea[A-Za-z0-9]*',line7)
                   if lemmatizer.lemmatize(word_verify_sea[0]) == 'sea':
                      line7 = line7.replace(word_verify_sea[0],"$")
                      line7 = line7.split()
                      for i in range(0,len(line7) - 2):
                          act_ngram6 = line7[i]+"_"+line7[i+1]+"_"+line7[i+2]
                          if '$' in act_ngram6:
                              list_of_ngrams.append(act_ngram6)


        for each_ngram in list_of_ngrams:
            print(each_ngram, separator, 1)
            
if __name__ == "__main__":
	main()

