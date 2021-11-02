import fcmRui
import random
import sys

def get_initial_sequence(alphabet, k):

    sequence = ""

    for i in range(0, k):
        sequence+=random.choice(alphabet)
    
    return sequence

def get_char(sequence, alphabet, k, prob_table):
    seq_index = fcmRui.get_index(sequence, alphabet, k)
    seq_probs = prob_table[seq_index]

    selected_char_num = random.random()

    for i in range(0,len(alphabet)):
        selected_char_num -= seq_probs[i]
        if selected_char_num <= 0:
            return alphabet[i]


def generate_text(file_name, k, alpha):
    alphabet, prob_table, total_entrophy = fcmRui.execute_fcm(file_name, k, alpha)

    text_lenght = 1000

    current_sequence = get_initial_sequence(alphabet, k)

    with open("generated_text.txt", 'w') as file:
        file.write(current_sequence)
        for i in range(2, text_lenght-k):
            next_char = get_char(current_sequence, alphabet, k, prob_table)
            current_sequence = current_sequence[1:] + next_char
            file.write(next_char)
        file.close()


def main():
    args = sys.argv[1:]

    if len(args)==0:
        raise Exception("Too little arguments")

    file_name = args[0]
    k = 1 if len(args)<2 else int(args[1])
    alpha = 1 if len(args)<3 else float(args[2])

    generate_text(file_name, k, alpha)


if __name__== "__main__":
    main()
