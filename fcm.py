def getWordsFromFile(file):
    f  = open(file, 'r')
    data = f.readlines()
    wordArray = []
    for line in data:
        wordArray += line.split()
    print(wordArray)

getWordsFromFile('bible.txt')
