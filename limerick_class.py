import random
from nltk.corpus import wordnet as wn
from nltk.corpus import words
from random import randint, sample
import pronouncing


class Limerick:
    line_1 = "empty"
    line_2 = "empty"
    line_3 = "empty"
    line_4 = "empty"
    line_5 = "empty"

    def __init__(self, subject_name):
        self.title = "An old limerick about " + subject_name + " #" + str(randint(0, 1000)) + ":"


    def set_line_1(self, new_line):
        self.line_1 = new_line

    def set_line_2(self, new_line):
        self.line_2 = new_line

    def set_line_3(self, new_line):
        self.line_3 = new_line

    def set_line_4(self, new_line):
        self.line_4 = new_line

    def set_line_5(self, new_line):
        self.line_5 = new_line


    def change_word(self, line_num, old_word, new_word):
        print('line to change in change word: ' + str(line_num))

        if line_num == 1:
            line = self.line_1 
        elif line_num == 2:
            line = self.line_2
        elif line_num == 3:
            line = self.line_3
        elif line_num == 4:
            line = self.line_4
        else:
            line = self.line_5
        
        print('old line: ' + line)
        new_line = line.replace(old_word, new_word)
        print('new line: ' + new_line)

        if line_num == 1:
            self.set_line_1(new_line)
        elif line_num == 2:
            self.set_line_2(new_line)
        elif line_num == 3:
            self.set_line_3(new_line)
        if line_num == 4:
            self.set_line_4(new_line)
        if line_num == 5:
            self.set_line_5(new_line)
        

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


def determine_fitness(limerick):
        fitness = 0
        # syllable check
        desired_line_syllables = [8.5, 8.5, 6.5, 6.5, 9.5]
        lines = [limerick.line_1, limerick.line_2, limerick.line_3, limerick.line_4, limerick.line_5]
        for i in range(5):
            limerick_words = lines[i].split(" ")
            line_syllables = 0
            for j in range(len(limerick_words)):
                word = limerick_words[j]
                phones = pronouncing.phones_for_word(word)
                counter = 0
                new_word = None
                while len(phones) < 1 and counter < 50:
                    print('found a not real word and trying synonyms: ' + word)
                    possible_word = find_synonym(word)
                    if possible_word == word:
                        possible_word = sample(words.words(), 1)[0]
                    print('new word = ' + possible_word)
                    phones = pronouncing.phones_for_word(possible_word)
                    counter += 1
                    new_word = possible_word
                if counter > 49:
                    print('hit max counter')
                    possible_word = sample(words.words(), 1)[0]
                    print('new word because of max: ' + possible_word)
                    phones = pronouncing.phones_for_word(possible_word)
                    while(len(phones) < 1):
                        possible_word = sample(words.words(), 1)[0]
                        phones = pronouncing.phones_for_word(new_word)
                        new_word = possible_word
                # this is where I need to replace the word
                
                if new_word != None:
                    print('line that must be changed is line :' + str(i + 1))
                    limerick.change_word(i+1, word, new_word)

                line_syllables += pronouncing.syllable_count(phones[0])
            fitness += (10 / abs(line_syllables - desired_line_syllables[i]))
        print(limerick)

        # grammar checks

        return fitness

def find_synonym(word):
    synonyms = []

    for syn in wn.synsets(word):    
        for l in syn.lemmas():
            if l.name() != word:
                synonyms.append(l.name())
    if len(synonyms) > 0:
        return random.choice(synonyms)

    else:
        return word



if __name__ == "__main__":
    print(pronouncing.phones_for_word('wrungness'))