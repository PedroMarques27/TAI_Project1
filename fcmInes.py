import re, copy
from typing import Text

from random import random

class FcmClass:

    def getExpressions(self):
        # remove all but words and spaces
        cleanData =self.data.lower()
        cleanData = re.sub("\s\s+", " ", cleanData)
        
        self.contextTable = {}
        self.alphabet = list(set(cleanData))

        # pass through all the characters and insert every 3 in the dict 
        # along with the next character and the times they appear
        
        # TODO adicionar as letras finais
        for i in range(len(cleanData)-self.k):
            expression = cleanData[i:i+self.k]
            
            if expression in self.contextTable.keys():
                if cleanData[i+self.k] in self.contextTable[expression]:
                    self.contextTable[expression][cleanData[i+self.k]] += 1   
                else:
                    self.contextTable[expression][cleanData[i+self.k]] = 1   
            else:
                self.contextTable[expression] = dict.fromkeys(self.alphabet, 0)
                self.contextTable[expression][cleanData[i+self.k]] = 1
            
        
        # print(str(expressionsDic))

        return self.contextTable


    def calculateProbabilityTable(self):
        self.probabilitiesTable = copy.deepcopy(self.contextTable)
        for expression in self.contextTable:
            total = 0;
            for char in self.contextTable[expression]:
                total+=self.contextTable[expression][char]

            for char in self.contextTable[expression]:
                occurences = self.contextTable[expression][char]
        
                self.probabilitiesTable[expression][char] = (occurences + self.a) / (total + (self.a * len(self.probabilitiesTable[expression])))
        
        
        
   

    def writeToFile(string, substring):
        f = open("output.txt", "w")
        substring = str(substring).replace("\n", "\\n")
        f.write(substring + "\n")
        f.write(str(string)+"\n")
        f.close()
    

    def getNextChar(self, expression):
 
        selectedChar = random()
        initialValue = 0
        # print(selectedChar)
        if expression not in self.probabilitiesTable:
            self.probabilitiesTable[expression]= dict.fromkeys(self.alphabet, (self.a) / ((self.a * len(self.alphabet)))) 
        # print(sorted(self.probabilitiesTable[expression]))
        for char in sorted(self.probabilitiesTable[expression]):
            #print(char +"+= " + str(initialValue) + ", " +str(initialValue+self.probabilitiesTable[expression][char]))
            if initialValue<=selectedChar < initialValue+self.probabilitiesTable[expression][char]:
                return char
            initialValue+= self.probabilitiesTable[expression][char]

    def __init__(self, filename="sherlock.txt", a=0.1, k=1):
        f  = open(filename, 'r')
        self.data = f.read()
        self.a = a
        self.k = k
    

