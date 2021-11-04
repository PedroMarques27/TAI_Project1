import sys

import time
import random
from fcm import fcm, get_index

def get_initial_sequence(alphabet, k):
    sequence = ""

    for i in range(0, k):
        sequence += random.choice(alphabet)

    return sequence

def generator(filename, alpha, k):

    table, probabilities_table,alphabet, entropy = fcm(filename, alpha,k)
    print('Total entropy: ' + str(entropy))

    text = get_initial_sequence(alphabet, k)


    i = 0
    while i < 1000:
        i += 1
        lastKcharacters = text[-k:]
        text+=get_next_char(probabilities_table,alphabet=alphabet, context=text, k=k, a=alpha)
    writeToFile(text)

def get_next_char(probabilities_table,alphabet, context,k, a):
    selected_char = random.random()
    initial_value = 0
    if type(probabilities_table) == dict:
        if context not in probabilities_table:
            probabilities_table[context]={}
        for char in alphabet:
            if char in probabilities_table[context]:
                prob = probabilities_table[context][char]
            else:
                prob = a / (a * len(alphabet))

            if initial_value <= selected_char < initial_value + prob:
                return char
            initial_value += prob
    else:
        index = int(get_index(context, alphabet, k=k))
        for i in range(len(alphabet)):
            if initial_value <= selected_char < initial_value + probabilities_table[index][i]:
                return alphabet[i]
            initial_value += probabilities_table[index][i]

def writeToFile(string):
    f = open("output.txt", "w", encoding='utf-8')
    f.write(str(string) + "\n")
    f.close()

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]
    k = 1 if len(args)<2 else int(args[1])
    alpha = 1 if len(args)<3 else float(args[2])

    starttime = time.time()
    generator(file_name, k=k, alpha=alpha)
    print('Time:' + str(time.time() - starttime) + "s")
    print('-' * 22)


if __name__== "__main__":
    main()
