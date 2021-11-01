import sys
import re
from pathlib import Path

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

    for i in range(len(file_text)-k):
        sequence = file_text[i:i+k]
        char = file_text[i+k]

        if type(table)==dict:
            if sequence not in table:
                table[sequence] = {c:1}
            else:
                if char not in table[sequence]:
                    table[sequence][char] = 1
                else:
                    table[sequence][char] += 1
        else:
            table[get_index(sequence, alphabet, k)][alphabet.index(char)] += 1 

    return table


def get_index(sequence, alphabet, k):

    a_size = len(alphabet)
    index = 0
    count = k-1

    for i in sequence:
        index += (a_size**count)*alphabet.index(i)
        count -= 1

    return index


def calculate_prob_table(table, alphabet, alpha):

    a_size = len(alphabet)
    prob_table = []

    for row in table:
        total = sum(row)
        prob_table.append([ ( (x+alpha) / (total+(alpha*a_size)) ) for x in row])

    return prob_table

def calculate_entrophy_table(prob_table, alphabet, alpha):

    return

def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]
    k = 1 if len(args)<2 else int(args[1])
    alpha = 1 if len(args)<3 else int(args[2])

    file_text = format_text(file_name)
    alphabet = get_alphabet(file_text)
    print(alphabet)
    table = make_table(alphabet, k)

    table = fill_table(file_text, alphabet, k, table)

    print(table)

    prob_table = calculate_prob_table(table, alphabet, alpha)
    
    print(prob_table)



if __name__== "__main__":
    main()