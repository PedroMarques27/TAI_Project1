import re
from typing import Text

def getExpressions(data, k):
    # remove all but words and spaces
    cleanData = re.sub(r'[^a-zA-Z ]+', '', data)
    cleanData = re.sub("\s\s+", " ", cleanData)
    
    expressionsDic = {}

    # pass through all the characters and insert every 3 in the dict 
    # along with the next character and the times they appear
    i = 0
    # TODO adicionar as letras finais
    while i<=(len(cleanData)-k-1):
        expression = cleanData[i:i+k]
        
        if expression in expressionsDic.keys():
            if cleanData[i+k] in expressionsDic[expression]:
                expressionsDic[expression][cleanData[i+k]] += 1   
            else:
                expressionsDic[expression][cleanData[i+k]] = 1   
        else:
            expressionsDic[expression] = {}
            expressionsDic[expression][cleanData[i+k]] = 1
        i+=1
    
    # print(str(expressionsDic))
    return expressionsDic

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

def init(filename, k):
    f  = open(filename, 'r')
    data = f.read()
    expressions_dict = getExpressions(data,k)
    text = generateText(expressions_dict, k)
    print("TEXT " + text)
    

init("sherlock.txt", 15)