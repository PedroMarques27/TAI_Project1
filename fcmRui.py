import sys
import re
from pathlib import Path
import math

def format_text(file_name):
    full_text = Path(file_name).read_text()
    full_text = re.sub('[^A-Za-z ]+', '', full_text)
    return full_text.lower()

def get_alphabet(file_text):
    return sorted(list(set(file_text)))

def calc_table_space(alphabet, k):
    a_size = len(alphabet)
    return (a_size ** k) * a_size * 16 / 8 / 1024 / 1024

def make_table(alphabet, k):

    occupied_space = calc_table_space(alphabet, k)
    a_size = len(alphabet)

    if occupied_space <= 256:
        table = [ [0]*a_size for x in range(a_size ** k) ]
    else:
        table = {}

    return table

def fill_table(file_text, alphabet, k, table):
    t1 = time.time()
    for i in range(len(file_text)-k):
        sequence = file_text[i:i+k]
        char = file_text[i+k]

        if type(table)==dict:
            if sequence not in table:
                table[sequence] = {char:1}
            else:
                if char not in table[sequence]:
                    table[sequence][char] = 1
                else:
                    table[sequence][char] += 1
        else:
            table[get_index(sequence, alphabet, k)][alphabet.index(char)] += 1 
    print(time.time() - t1)
    return table


def get_index(sequence, alphabet, k):

    a_size = len(alphabet)
    index = 0
    count = k-1

    for i in sequence:
        index += (a_size**count)*alphabet.index(i)
        count -= 1

    return index


def calc_prob_entrophy_table(table, alphabet, alpha, total_sequences):
    #versao de dicionario?
    a_size = len(alphabet)
    prob_table = []

    total_entrophy = 0

    for row in table:
        total = sum(row)
        prob_row = [ ( (x+alpha) / (total+(alpha*a_size)) ) for x in row]
        prob_table.append(prob_row)
        ent_row = -sum([x*math.log2(x) for x in prob_row])
        total_entrophy += (total/total_sequences) * ent_row

    return prob_table, total_entrophy

def execute_fcm(file_name, k , alpha):

    file_text = format_text(file_name)
    alphabet = get_alphabet(file_text)

    table = make_table(alphabet, k)

    table = fill_table(file_text, alphabet, k, table)

    total_sequences = len(file_text)-k

    prob_table, total_entrophy = calc_prob_entrophy_table(table, alphabet, alpha, total_sequences)

    print("Total entropy of the text: " + str(total_entrophy))

    return alphabet, prob_table, total_entrophy

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]
    k = 1 if len(args)<2 else int(args[1])
    alpha = 1 if len(args)<3 else float(args[2])

    execute_fcm(file_name, k, alpha)


if __name__== "__main__":
    main()