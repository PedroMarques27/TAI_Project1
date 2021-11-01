from fcmInes import FcmClass 
import random
from random import randint
def generator(filename, alpha, k):
    fcm = FcmClass(filename, alpha,k)
    fcm.getExpressions()
    fcm.calculateProbabilityTable()
    value = randint(0, len(fcm.contextTable.keys()))
    text = list(fcm.contextTable.keys())[value]

   
    i = 0
    while i < len(fcm.data):
        i += 1
        lastKcharacters = text[-k:]
        text+=fcm.getNextChar(lastKcharacters)
    fcm.writeToFile(text)
    print(text)
generator("sherlock.txt", 0.1, 3)