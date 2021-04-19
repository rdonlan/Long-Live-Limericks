from limerick_class import Limerick, determine_fitness
# from nltk.corpus.reader import verbnet
# from nltk.corpus.reader.wordlist import WordListCorpusReader
import pronouncing
# import nltk
from nltk.corpus import words
# nltk.download('words')


from Phyme import Phyme
ph = Phyme()

import nltk
from nltk.corpus import wordnet as wn

from random_word import RandomWords
ra = RandomWords()

import random
from random import sample

from wonderwords import RandomWord
r = RandomWord()
from wonderwords import RandomSentence
s = RandomSentence()

# global variables
DETERMINERS = ['all', 'an', 'another', 'any', 'both', 'each', 'either', 'every', 'many',
     'no', 'some', 'such', 'that', 'the', 'these', 'this', 'those']
AUXILARY = ["can", "cannot", "could", "couldn't", "dare", "may", "might", "must", "need", "ought", "shall", "should",
"shouldn't", "will", "would",]

'''
n = NOUN

v = VERB

a = ADJECTIVE

r = ADVERB
'''

def find_rhyme(word, type_of_word=None):
    possible_rhymes = ph.get_perfect_rhymes(word)
    rhyming_words_list = []
    for entry in possible_rhymes.values():
        rhyming_words_list += entry

    rhymed_word = random.choice(rhyming_words_list)

    while('1' in rhymed_word or rhymed_word == word):
        rhymed_word = random.choice(rhyming_words_list)

    rhymed_word_type = None

    if wn.synsets(rhymed_word) != []:
        rhymed_word_type = wn.synsets(rhymed_word)[0].pos()

    if type_of_word != None:
        while(rhymed_word_type != type_of_word and len(rhyming_words_list) > 0):
            rhymed_word = random.choice(rhyming_words_list)
            if wn.synsets(rhymed_word) != []:
                rhymed_word_type = wn.synsets(rhymed_word)[0].pos()

            else:
                rhymed_word_type = None
            rhyming_words_list.remove(rhymed_word)

    if rhymed_word[-1] == ')':
        rhymed_word = rhymed_word[:-3]

    return rhymed_word


def original_generate_first_line(limerick_obj, name, pronoun):
    first_line = "Once there was "
    adjective = r.word(include_parts_of_speech=["adjectives"])
    if adjective[0] in ['a', 'e', 'i', 'o', 'u']:
        first_line = first_line + 'an '
    else:
        first_line = first_line + 'a '
    first_line = first_line + adjective + ' '
    if pronoun == 'he':
        first_line = first_line + "lad "
    else:
        first_line = first_line + "lassie "
    first_line = first_line + 'named ' + name

    limerick_obj.add_line(1, first_line)


def original_generate_second_line(limerick_obj, name, pronoun):

    second_line = pronoun + ' '
    verb = r.word(include_parts_of_speech=["verb"])
    if verb[-1] == 'e':
        verb = verb + 'd '
    else:
        verb = verb + 'ed '
    second_line = second_line + verb
    second_line = second_line + random.choice(DETERMINERS) + ' '
    adjective = r.word(include_parts_of_speech=["adjective"])
    second_line = second_line + adjective + ' '

    rhyming_words = ph.get_perfect_rhymes(name)
    rhyming_words_list = []
    for entry in rhyming_words.values():
        rhyming_words_list += entry

    second_line = second_line + random.choice(rhyming_words_list)

    limerick_obj.add_line(2, second_line)


def original_generate_3rd_4th_lines(limerick_obj, pronoun):

    line_type = random.randint(0,2)

    random_determinant_1 = random.choice(DETERMINERS)
    random_determinant_2 = random.choice(DETERMINERS)
    random_determinant_3 = random.choice(DETERMINERS)
    random_determinant_4 = random.choice(DETERMINERS)
    random_auxilary_1 = random.choice(AUXILARY)
    random_auxilary_2 = random.choice(AUXILARY)
    random_noun = r.random_words(3, include_parts_of_speech=["noun"])
    random_verb_ing = r.random_words(2, include_parts_of_speech=["verb"], ends_with='ing')
    random_verb = r.random_words(3, include_parts_of_speech=["verb"])
    random_adverb = r.random_words(3, include_parts_of_speech=[], ends_with='ly')

    if line_type == 0:
        # determinant, noun, verb
        line_3 = random_determinant_1 + ' ' + random_noun[0] + ' ' + random_determinant_2 + ' ' + random_verb[0]
        limerick_obj.add_line(3, line_3)

        rhymed_word = find_rhyme(random_verb[0])

        line_4 = random_determinant_3 + ' ' + random_noun[1] + ' ' + random_determinant_4 + ' ' + rhymed_word
        limerick_obj.add_line(4, line_4)


    elif line_type == 1:
        # verb, adverb, name, determinant
        line_3 = random_verb[0] + ' ' + random_adverb[0] + ' did ' + pronoun
        limerick_obj.add_line(3, line_3)

        rhymed_word = find_rhyme(pronoun)

        line_4 = 'the ' + random_noun[0] + ' ' + random_verb[1] + ' ' + rhymed_word
        limerick_obj.add_line(4, line_4)

    elif line_type == 2:
        # noun determinant noun adverb verb
        line_3 = random_noun[0] + ' and ' + random_noun[1] + ' ' + random_auxilary_1 + ' be ' + random_verb[0]
        limerick_obj.add_line(3, line_3)

        rhymed_word = find_rhyme(random_verb[0])

        line_4 = random_determinant_1 + ' ' + random_noun[2] + ' ' + random_verb[1] + ' ' + random_auxilary_2 + ' ' + rhymed_word
        limerick_obj.add_line(4, line_4)




def original_generate_5th_line(limerick_obj, name, pronoun):
    rhymed_word = find_rhyme(name)
    # determinant, noun, auxillary
    line_5 = random.choice(DETERMINERS) + ' ' + r.word(include_parts_of_speech=["noun"]) + ' ' + pronoun \
    + ' ' + random.choice(AUXILARY) + ' ' + rhymed_word
    limerick_obj.add_line(5, line_5)

    

def generate_limerick(limerick_obj, name, pronoun):
    original_generate_first_line(limerick_obj, name, pronoun)
    original_generate_second_line(limerick_obj, name, pronoun)
    original_generate_3rd_4th_lines(limerick_obj, pronoun)
    original_generate_5th_line(limerick_obj, name, pronoun)





if __name__ == "__main__":

    # name = input('Enter who/what will the limerick be about (proper or regular noun): ')
    # pronoun = input('Is your object a: He | She | It : ').lower()

    name = 'Swank'
    pronoun = 'he'

    limerick_1 = Limerick(name)
    generate_limerick(limerick_1, name, pronoun)
    determine_fitness(limerick_1)

    print('\n')

    limerick_2 = Limerick(name)
    generate_limerick(limerick_2, name, pronoun)
    determine_fitness(limerick_2)

    print('\n')

    limerick_3 = Limerick(name)
    generate_limerick(limerick_3, name, pronoun)
    determine_fitness(limerick_3)

    print('\n')

    
    # print(' '.join(sample(words.words(), 1)))
    # print(find_synonym('forbided'))