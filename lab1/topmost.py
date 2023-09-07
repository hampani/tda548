import wordfreq
import sys
import urllib.request

stopWords = sys.argv[1]
text = sys.argv[2]
numberOfWords = sys.argv[3]

def readFile(fileName):
    file = open(fileName, encoding="utf-8")
    lines = file.read().split('\n')
    file.close()
    return lines

def main():
    stopWordsLines = readFile(stopWords)

    if (text.startswith("http://") or text.startswith("https://")):
        response = urllib.request.urlopen(sys.argv[2])
        textLines = response.read().decode("utf8").splitlines()
    else:
        textLines = readFile(text)
    
    words = wordfreq.tokenize(textLines)
    frequencies = wordfreq.countWords(words, stopWordsLines)
    wordfreq.printTopMost(frequencies, int(numberOfWords))
    
if __name__ == "__main__":
    main()