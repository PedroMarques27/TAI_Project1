import sys

from fcm import FcmClass
import random
from random import randint

def generator(filename, alpha, k):
    fcm = FcmClass(filename, alpha,k)
    fcm.get_expressions_from_data()
    print('Finished Reading File...')
    fcm.get_probability_table()
    print('Finished calculating probabilities...')
    print('Total entropy: ' + str(fcm.get_table_entropy()))
    print('Generating text...')
    if type(fcm.table) == dict:
        value = randint(0, len(fcm.table))
        text = list(fcm.table.keys())[value]

    else:
        value = randint(0, len(fcm.expressions))
        text = fcm.expressions[value]


    i = 0
    while i < 10000:
        i += 1
        lastKcharacters = text[-k:]
        text+=fcm.get_next_char(lastKcharacters)
    writeToFile(text)
    print(text)

def writeToFile(string):
    f = open("output.txt", "w", encoding='utf-8')
    f.write(str(string) + "\n")
    f.close()

def main():
    '''
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]
    k = 1 if len(args)<2 else int(args[1])
    alpha = 1 if len(args)<3 else float(args[2])

    generator(file_name, k, alpha)
    '''

    generator("sherlock.txt", 0.1, 3)
if __name__== "__main__":
    main()
