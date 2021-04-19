import random
from nltk.corpus import wordnet as wn
from random import randint
import pronouncing


class Limerick:
    line_1 = "empty"
    line_2 = "empty"
    line_3 = "empty"
    line_4 = "empty"
    line_5 = "empty"

    def __init__(self, subject_name):
        self.title = "An old limerick about " + subject_name + " #" + str(randint(0, 1000)) + ":"

    # this method adds lines to limerick object
    def add_line(self, line_num, line):
        if line_num == 1:
            self.line_1 = line
        if line_num == 2:
            self.line_2 = line
        if line_num == 3:
            self.line_3 = line
        if line_num == 4:
            self.line_4 = line
        if line_num == 5:
            self.line_5 = line
            


    def __str__(self):
        # allows you to use print(Recipe)
        final_string = self.title + "\n"
        final_string += self.line_1 + "\n"
        final_string += self.line_2 + "\n"
        final_string += self.line_3 + "\n"
        final_string += self.line_4 + "\n"
        final_string += self.line_5
        return final_string    


def determine_fitness(self):
        fitness = 0
        # syllable check
        desired_line_syllables = [8.5, 8.5, 6.5, 6.5, 9.5]
        lines = [self.line_1, self.line_2, self.line_3, self.line_4, self.line_5]
        for i in range(len(lines)):
            words = lines[i].split(" ")
            line_syllables = 0
            for j in range(len(words)):
                phones = pronouncing.phones_for_word(words[j])
                if len(phones) < 1:
                    print('found a not real word and trying synonyms')
                    new_word = find_synonym(words[j])
                    words[j] = new_word
                    phones = pronouncing.phones_for_word(new_word)
                line_syllables += pronouncing.syllable_count(phones[0])
            print(line_syllables)
            fitness += (10 / abs(line_syllables - desired_line_syllables[i]))
        print(fitness)
        print(self)

        # grammar checks

        return fitness

def find_synonym(word):
    synonyms = []

    for syn in wn.synsets(word):    
        for l in syn.lemmas():
            if l.name() != word:
                synonyms.append(l.name())

    return random.choice(synonyms)



