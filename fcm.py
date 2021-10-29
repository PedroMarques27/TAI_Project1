def getWordsFromFile(data,k):
    
    dataset = []
    i = 0
    while i<=len(data):
        word = data[i:i+k]
        i+=1
        dataset.append(word)
    return set(dataset)         #gets all possible character sequences with length k


def find_all(data, substring):
    start = 0
    occurences = []
    while True:
        start = data.find(substring, start)
        if start == -1: return
        start += len(substring)
        occurences+=[start]     #gets all index where substring starts

def init(file, k, alpha):
    f  = open(file, 'r')
    data = f.read()
    dataset = getWordsFromFile(data,k)
    

getWordsFromFile('bible.txt',3)
