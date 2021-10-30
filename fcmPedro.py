def getWordsFromFile(data,k):
    characters = []
    dataset = []
    i = 0
    while i<=len(data):
        word = data[i:i+k]
        i+=1
        dataset.append(word.lower())
        for char in word:
            characters.append(char.lower())
    return set(dataset), set(characters)         #gets all possible character sequences with length k


def find_all(data, substring):
    start = 0
    occurences = []
    while True:
        start = data.find(substring, start)

        if start == -1 or start >= len(data): return occurences
        occurences+=[start]
        start+=len(substring)
        
    print(occurences)   #gets all index where substring starts

def init(file, k, alpha):
    f  = open(file, 'r')
    data = f.read()
    dataset, chars = getWordsFromFile(data,k)
  
    count(chars, dataset, data, k)

def count(universe, dataset, data,k):
    for word in dataset:
        if len(str(word))>0: 
            counting = dict.fromkeys(universe, 0)
            occ = find_all(data, word)
            for o in occ:
                if o+k<len(data):
                    counting[data[o+k].lower()]+=1
            writeToFile(counting, word)
       
def writeToFile( data, substring):
    f = open("output.txt", "a")
    substring = substring.replace("\n", "\\n")
    f.write(substring + "\n")
    f.write(str(data)+"\n")
    f.close()
        
init('bible.txt',3,2)