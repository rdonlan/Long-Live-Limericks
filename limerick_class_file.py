'''
inspiration
http://www.eecs.qmul.ac.uk/~mpurver/papers/mcgregor-et-al16ccnlg.pdf
'''
# imports
import os
import random
from nltk.corpus import wordnet as wn
from nltk.corpus import words
from random import randint, sample
import pronouncing
from Phyme import Phyme
ph = Phyme()

'''
The limerick class is a roadmap for limerick objects that will each contain their 5 lines, and also different
methods that will allow the printing and reading of the limericks. Also, getters and setters were created to
allow the program to change lines of the limericks when required.
'''
class Limerick:
    line_1 = "empty"
    line_2 = "empty"
    line_3 = "empty"
    line_4 = "empty"
    line_5 = "empty"

    def __init__(self, subject_name, pronoun):
        if pronoun == 'it':
            self.title = "An old limerick about a " + subject_name + " #" + str(randint(0, 1000)) + ":"
        else:
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

    def get_line_1(self):
        return self.line_1

    def get_line_2(self):
        return self.line_2

    def get_line_3(self):
        return self.line_3

    def get_line_4(self):
        return self.line_4

    def get_line_5(self):
        return self.line_5


    '''
    This method changes a singular word on a singular line of the limerick object this method
    is called on.
        Params:
            @self {Limerick obj}: the limerick that is being altered
            @line_num {int}: the line of the limerick that is being altered
            @old_word {str}: the word that is being replaced from the limerick
            @new_word {str}: the word that is being slot into the limerick for the old_word
        Return:
            None
    '''
    def change_word(self, line_num, old_word, new_word):

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
        
        new_line = line.replace(old_word, new_word)

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
            

    '''
    This string funtion prints all 5 lines of the limerick object it is called on. 
    '''
    def __str__(self):
        # allows you to use print(limerick)
        final_string = self.title + "\n"
        final_string += self.line_1 + "\n"
        final_string += self.line_2 + "\n"
        final_string += self.line_3 + "\n"
        final_string += self.line_4 + "\n"
        final_string += self.line_5
        return final_string    

    
    '''
    This method uses the OS to read alound the limerick that it was called by.
    '''
    def read_limerick(self):
        os.system("say -v Alex " + self.get_line_1() )
        os.system("say -v Alex " + self.get_line_2() )
        os.system("say -v Alex " + self.get_line_3() )
        os.system("say -v Alex " + self.get_line_4() )
        os.system("say -v Alex " + self.get_line_5() )


'''
This method calculates the syllable fitness of the limerick. The meter of a limerick is very important, as it
is supposed to have an emphasis on traditional syllables in a word, which can only be possible if there is a
specific amount of syllables in each line. This method checks the amount of syllables in each line against the 
desired amount of syllables (there is an arr with these values in the method). There are some instances when the
syllable counter doesn't know a word it encounters, so the method tries to find a synonyms for the unknown word
to keep the meaning and still count the syllables. If that isn't possible then a random word is chosen. If a different 
word has to be chosen then it is added into the limerick instead of the word that couldn't have its syllables determined.
This score will end up being out of 100.
    Params:
        @self {Limerick obj}: the limerick that's fitness is being determined
    Return:
        @fitness {int}: the syllable fitness of the limerick that was calculated
'''
def syllable_fitness(limerick):
        fitness = 0
        # these values are not whole numbers so there is no divide by 0 error when calculating 
        # fitness at the end of the function
        desired_line_syllables = [9.5, 8.5, 7.5, 7.5, 9.5]
        lines = [limerick.line_1, limerick.line_2, limerick.line_3, limerick.line_4, limerick.line_5]
        # for every line in the limerick
        for i in range(5):
            limerick_words = lines[i].split(" ")
            line_syllables = 0
            # for every word in each line
            for j in range(len(limerick_words)):
                word = limerick_words[j]
                phones = pronouncing.phones_for_word(word)
                counter = 0
                new_word = None
                # if this while statement is triggered it means that we can't determine the number 
                # of syllables in the word this is because pronouncing doesn't have the word in its 
                # dictionary or the word isn't a real word
                while len(phones) < 1 and counter < 50:
                    possible_word = find_synonym(word)
                    # making sure the synonym isn't the same as the word we are trying to change
                    if possible_word == word:
                        # generate a random word in the hopes that its syllables can be calculated
                        possible_word = sample(words.words(), 1)[0]
                    phones = pronouncing.phones_for_word(possible_word)
                    counter += 1
                    new_word = possible_word
                # if a synonyms can't be found after 50 tries we generate a random word over and over
                # until we are sure we can count its syllables
                if counter > 49:
                    possible_word = sample(words.words(), 1)[0]
                    phones = pronouncing.phones_for_word(possible_word)
                    # once again making sure the random word can be checked for syllables
                    while(len(phones) < 1):
                        possible_word = sample(words.words(), 1)[0]
                        phones = pronouncing.phones_for_word(new_word)
                        new_word = possible_word
                
                # need to replace the previous word with the new one in the limerick
                if new_word != None:
                    limerick.change_word(i+1, word, new_word)

                line_syllables += pronouncing.syllable_count(phones[0])
            fitness += (10 / abs(line_syllables - desired_line_syllables[i]))

        return fitness


'''
This method calculates the rhyming fitness of the limerick. The rhyming scheme of a limerick is
AABBA, so it checks all 4 relationships and subtracts points from a starting score of 50. Then this
score is return after being multiplied by 2 so it is out of 100.
    Params:
        @self {Limerick obj}: the limerick that's fitness is being determined
    Return:
        @rhyming_fitness {int}: the rhyming fitness of the limerick that was calculated
'''
def rhyming_fitness(limerick):
    rhyming_fitness = 50

    last_word_line_1 = limerick.line_1.split(' ')[-1]
    last_word_line_2 = limerick.line_2.split(' ')[-1]
    last_word_line_5 = limerick.line_5.split(' ')[-1]

    if do_they_rhyme(last_word_line_1, last_word_line_2) is False:
        rhyming_fitness -= 10

    if do_they_rhyme(last_word_line_2, last_word_line_5) is False:
        rhyming_fitness -= 10

    if do_they_rhyme(last_word_line_1, last_word_line_5) is False:
        rhyming_fitness -= 10


    last_word_line_3 = limerick.line_3.split(' ')[-1]
    last_word_line_4 = limerick.line_4.split(' ')[-1]

    if do_they_rhyme(last_word_line_3, last_word_line_4) is False:
        rhyming_fitness -= 20

    return 2 * rhyming_fitness


'''
This method finds a synonyms for the given word. If one can't be found then a random word is returned.
    Params:
        @word {str}: the word that the method is finding a synonyms for
    Return:
        string --> a string synonyms is returned, or if none were found then the parameter word is returned
'''
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


'''
This method checks if two words rhyme.
    Params:
        @word1 {str}: the first word being checkec
        @word2 {str}: the second word being checked
    Return:
        boolean --> True if they rhyme, False if they don't
'''
def do_they_rhyme(word1, word2):
    possible_rhymes = pronouncing.rhymes(word1)
    if word2 in possible_rhymes:
        return True
    else:
        return False