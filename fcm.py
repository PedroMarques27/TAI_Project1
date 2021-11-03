import math
import re, copy
from typing import Text
import sys
from random import random


class FcmClass:

    def make_table(self):
        occupied_space = self.get_table_space()
        a_size = len(self.alphabet)
        if occupied_space <= 256:
            self.table = [[0] * a_size for x in range(a_size ** self.k)]
        else:
            self.table = {}
        return self.table

    def get_normalized_string(self):
        # remove all but words and spaces
        self.data = re.sub(r'[^a-zA-Z ]+', '', self.data.lower())
        self.data = re.sub("\s\s+", " ", self.data)
        return self.data

    def get_alphabet(self):
        self.alphabet = sorted(list(set(self.data)))
        return self.alphabet

    def get_expressions_from_data(self):
        # pass through all the characters and insert every 3 in the dict 
        # along with the next character and the times they appear
        for i in range(len(self.data) - self.k):
            context = self.data[i:i + self.k]
            next_char = self.data[i + self.k]

            if type(self.table) == dict:
                if context in self.table:
                    if next_char in self.table[context]:
                        self.table[context][next_char] += 1
                    else:
                        self.table[context][next_char] = 1
                else:
                    self.table[context] = {next_char: 1}
            else:
                self.table[self.get_index(context)][self.alphabet.index(next_char)] += 1
        return self.table

    def get_index(self, context):
        a_size = len(self.alphabet)
        index = 0
        count = self.k - 1

        for i in context:
            index += (a_size ** count) * self.alphabet.index(i)
            count -= 1

        return index


    def get_table_space(self):
        a_size = len(self.alphabet)
        return (a_size ** self.k) * a_size * 16 / 8 / 1024 / 1024

    def get_probability_table(self):
        self.probabilities_table = copy.deepcopy(self.table)
        if type(self.table) == dict:
            for context in self.table:
                total = sum(self.table[context].values())
                for char in self.table[context]:
                    occurrence = self.table[context][char]
                    self.probabilities_table[context][char] = self.get_probability(occurrence, total)
        else:
            for x in range(len(self.alphabet) ** self.k):
                total = sum(self.table[x])
                self.probabilities_table[x] = [self.get_probability(occurrence, total) for occurrence in self.table[x]]

    def get_probability(self, occurrence, total):
        return (occurrence + self.a) / (total + (self.a * len(self.alphabet)))

    def get_table_entropy(self):

        total_entropy = 0
        total_sequences = len(self.data)-self.k
        if type(self.table) == dict:
            for i in range(len(self.probabilities_table)):
                total = sum(self.table[i].values())
                ent_row = -sum([x * math.log2(x) for x in self.probabilities_table[i].values()])
                total_entropy += (total / total_sequences) * ent_row
        else:
            for i in range(len(self.probabilities_table)):
                total = sum(self.table[i])
                ent_row = -sum([x * math.log2(x) for x in self.probabilities_table[i]])
                total_entropy += (total / total_sequences) * ent_row

        return total_entropy

    def get_next_char(self, context):
        selected_char = random()
        initial_value = 0
        if type(self.table) == dict:
            if context not in self.probabilities_table:
                self.probabilities_table[context] = dict.fromkeys(self.alphabet, self.a / (self.a * len(self.alphabet)))
            for char in sorted(self.probabilities_table[context]):
                if initial_value <= selected_char < initial_value + self.probabilities_table[context][char]:
                    return char
                initial_value += self.probabilities_table[context][char]
        else:
            index = self.get_index(context)
            for i in range(len(self.alphabet)):
                if initial_value <= selected_char < initial_value + self.probabilities_table[index][i]:
                    return self.alphabet[i]
                initial_value += self.probabilities_table[index][i]

    def __init__(self, filename="sherlock.txt", a=0.1, k=1):
        f = open(filename, 'r')
        self.expressions = []
        self.table = []
        self.probabilities_table = []
        self.alphabet = []
        self.a = a
        self.k = k
        self.data = f.read()
        self.get_normalized_string()
        self.get_alphabet()
        self.make_table()

fcm = FcmClass("sherlock.txt", 0.1, 3)
fcm.get_expressions_from_data()
print('Finished Reading File...')
fcm.get_probability_table()
print('Finished calculating probabilities...')
print('Total entropy: ' + str(fcm.get_table_entropy()))
print('Generating text...')