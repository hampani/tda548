import wordfreq
import sys
import urllib.request

stopWords = sys.argv[1]
text = sys.argv[2]
numberOfWords = sys.argv[3]

def main():
    stopWordsFile = open(stopWords, encoding="utf-8")
    stopWordsLines = stopWordsFile.read().split('\n')
    stopWordsFile.close()

    if (text.startswith("http://") or text.startswith("https://")):
        response = urllib.request.urlopen(sys.argv[2])
        textLines = response.read().decode("utf8").splitlines()
    else:
        textFile = open(text, encoding="utf-8")
        textLines = textFile.read().split('\n')
        textFile.close()
    
    words = wordfreq.tokenize(textLines)
    frequencies = wordfreq.countWords(words, stopWordsLines)
    wordfreq.printTopMost(frequencies, int(numberOfWords))
    
if __name__ == "__main__":
    main()