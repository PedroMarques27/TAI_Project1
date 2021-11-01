import re, copy
from typing import Text

def getExpressions(data, k):
    # remove all but words and spaces
    cleanData = re.sub(r'[^a-zA-Z ]+', '', data).lower()
    cleanData = re.sub("\s\s+", " ", cleanData)
    
    expressionsDic = {}
    alphabet = list(set(cleanData))

    # pass through all the characters and insert every 3 in the dict 
    # along with the next character and the times they appear
    
    # TODO adicionar as letras finais
    for i in range(len(cleanData)-k):
        expression = cleanData[i:i+k]
        
        if expression in expressionsDic.keys():
            if cleanData[i+k] in expressionsDic[expression]:
                expressionsDic[expression][cleanData[i+k]] += 1   
            else:
                expressionsDic[expression][cleanData[i+k]] = 1   
        else:
            expressionsDic[expression] = dict.fromkeys(alphabet, 0)
            expressionsDic[expression][cleanData[i+k]] = 1
        
    
    # print(str(expressionsDic))

    return expressionsDic


def calculateProbability(dictionary, a):
    probabilities = copy.deepcopy(dictionary)
    for expression in dictionary:
        total = 0;
        for char in dictionary[expression]:
            total+=dictionary[expression][char]

        for char in dictionary[expression]:
            occurences = dictionary[expression][char]
     
            probabilities[expression][char] = (occurences + a) / (total + (a * len(probabilities[expression])))

    
    
def generateText(expressionsDic, k):
    text = list(expressionsDic.keys())[0]
    
    # print(text)
    i = 0
    while i < 500:
        i += 1
        lastKcharacters = text[-k:]
        dictMatch = expressionsDic[lastKcharacters] # returns dict
        # maxValue = max(dictMatch.values())
        maxKey = max(dictMatch, key=dictMatch.get)
        text += maxKey

    return text

def writeToFile( data, substring):
    f = open("output.txt", "w")
    substring = str(substring).replace("\n", "\\n")
    f.write(substring + "\n")
    f.write(str(data)+"\n")
    f.close()
        
def init(filename, k):
    f  = open(filename, 'r')
    data = f.read()
    expressions_dict = getExpressions(data,k)
    calculateProbability(expressions_dict, 0.01)

    text = generateText(expressions_dict, k)
    print("TEXT " + text)
    

init("sherlock.txt", 3)