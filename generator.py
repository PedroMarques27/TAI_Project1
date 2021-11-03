import sys

from fcm import FcmClass
import time
import random
from random import randint


def get_initial_sequence(alphabet, k):
    sequence = ""

    for i in range(0, k):
        sequence += random.choice(alphabet)

    return sequence
def generator(filename, alpha, k):
    fcm = FcmClass(filename, alpha,k)
    fcm.get_expressions_from_data()
    fcm.get_probability_table()
    print('Total entropy: ' + str(fcm.entropy))

    text = get_initial_sequence(fcm.alphabet, k)


    i = 0
    while i < 1000:
        i += 1
        lastKcharacters = text[-k:]
        text+=fcm.get_next_char(lastKcharacters)
    writeToFile(text)

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
    print('-'*22)
    starttime = time.time()
    generator("sherlock.txt", 0.1, 3)
    print('Time:' + str(time.time() - starttime)+"s")
    print('-'*22)
    starttime = time.time()
    generator("sherlock.txt", 0.1, 4)
    print('Time:' + str(time.time() - starttime)+"s")
    print('-'*22)
    starttime = time.time()
    generator("sherlock.txt", 0.1, 5)
    print('Time:' + str(time.time() - starttime)+"s")
    print('-'*22)
    starttime = time.time()
    generator("sherlock.txt", 0.1, 6)
    print('Time:' + str(time.time() - starttime)+"s")
    print('-'*22)
    starttime = time.time()
    generator("sherlock.txt", 0.1, 7)
    print('Time:' + str(time.time() - starttime)+"s")
    print('-'*22)
if __name__== "__main__":
    main()
