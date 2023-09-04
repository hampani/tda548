def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        line = line.lower()
        while start < len(line):
            while(start < len(line) and line[start].isspace()):
                start += 1

            end = start
            if (start < len(line)):
                if line[start].isdigit():
                    while(end < len(line) and line[end].isdigit()):
                        end += 1
                    words.append(line[start:end])
                    start = end - 1
                elif line[start].isalpha():
                    while(end < len(line) and line[end].isalpha()):
                        end += 1
                    words.append(line[start:end])
                    start = end - 1
                else:
                    words.append(line[start])

            start += 1

    return words

def countWords(words, stopWords):
    frequencies = {}
    for word in words:
        if word in stopWords:
            continue
        if word not in frequencies:
            frequencies.update({word: 1})
        else:
            frequencies.update({word: frequencies.get(word) + 1})
    return frequencies

def printTopMost(frequencies, n):
    sortedFrequencies = dict(sorted(frequencies.items(), key=lambda x: -x[1]))
    for idx, word in enumerate(sortedFrequencies):
        if (idx >= n): break
        print(word.ljust(20), frequencies.get(word))