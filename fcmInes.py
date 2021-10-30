import re

def getExpressions(data, k):
    # remove all but words and spaces
    cleanData = re.sub(r'[^a-zA-Z ]+', '', data)
    expressionsDic = {}

    # pass through all the characters and insert every 3 in the dict 
    # along with the next character and the times they appear
    i = 0
    while i<=len(cleanData):
        expression = cleanData[i:i+k]
        i+=1
        print(str(expressionsDic))
        if expression in expressionsDic.keys():
            if cleanData[i+k] in expressionsDic[expression]:
                expressionsDic[expression][cleanData[i+k]] += 1   
            else:
                expressionsDic[expression][cleanData[i+k]] = 1   
        else:
            expressionsDic[expression] = {}
            expressionsDic[expression][cleanData[i+k]] = 1

    # print(str(expressionsDic))

    return expressionsDic

def init(filename, k):
    f  = open(filename, 'r')
    data = f.read()
    expressions_dict = getExpressions(data,k)
    

init("example.txt", 3)