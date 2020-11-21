import sys
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

def main():
    stop_words = set(stopwords.words('english'))
    for line in sys.stdin:

      # Remove trailing spaces 
      line = line.strip()
      # Convert the line into lowercase
      line = line.lower()
      line = line.replace('_','')

      line = line.rstrip()
      # Remove alphanumeric symbols and tokenize into words.
      tokenizer = nltk.RegexpTokenizer(r"\w+")
      words = tokenizer.tokenize(line)

      for word in words:
          word = re.sub(r'\d+', '', word)
          # Remove stopwords and invalid words.
          if word not in stop_words and word != "":
              print(word,"1")

if __name__ == "__main__":
	main()

    
	
