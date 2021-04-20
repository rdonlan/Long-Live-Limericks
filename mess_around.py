from limerick_class_file import Limerick, syllable_fitness, rhyming_fitness
from rank_select import rank_selection, rank_selection_cum_prob_list, sort_by_rank
from recombination_and_mutation import make_next_gen
from nltk.corpus import words



from Phyme import Phyme
ph = Phyme()

from nltk.corpus import wordnet as wn

from random_word import RandomWords
ra = RandomWords()

import random

from wonderwords import RandomWord
r = RandomWord()
from wonderwords import RandomSentence
s = RandomSentence()

# global variables
DETERMINERS = ['all', 'an', 'another', 'any', 'both', 'each', 'either', 'every', 'many',
     'no', 'some', 'such', 'that', 'the', 'these', 'this', 'those']
AUXILARY = ["can", "cannot", "could", "couldn't", "dare", "may", "might", "must", "need", "ought", "shall", "should",
"shouldn't", "will", "would",]
MUTATION_RATE = 0.01
TOTAL_GENERATIONS = 2
POPULATION_SIZE = 4


'''
n = NOUN

v = VERB

a = ADJECTIVE

r = ADVERB
'''

def find_rhyme(word, type_of_word=None):
    try:
        possible_rhymes = ph.get_perfect_rhymes(word)
    # this error occurs when the word is not in Phyme's dictionary
    except KeyError:
        return word


    rhyming_words_list = []
    for entry in possible_rhymes.values():
        rhyming_words_list += entry
    rhymed_word = random.choice(rhyming_words_list)

    # makes sure the word only has letters in it
    counter = 0
    while(('1' in rhymed_word or rhymed_word == word) and counter < 50):
        rhymed_word = random.choice(rhyming_words_list)
        counter += 1

    # couldn't find a rhyme so picks a random word
    if counter > 49:
        rhymed_word = random.sample(words.words(), 1)[0]

    rhymed_word_type = None

    if wn.synsets(rhymed_word) != []:
        rhymed_word_type = wn.synsets(rhymed_word)[0].pos()

    # if the program is looking for a specific type (noun, adj, verb, adverb) of rhymed word
    if type_of_word != None:
        while(rhymed_word_type != type_of_word and len(rhyming_words_list) > 0):
            rhymed_word = random.choice(rhyming_words_list)
            if wn.synsets(rhymed_word) != []:
                rhymed_word_type = wn.synsets(rhymed_word)[0].pos()

            else:
                rhymed_word_type = None
            rhyming_words_list.remove(rhymed_word)

    # again making sure the word is only letters
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
    first_line = first_line + adjective
    if pronoun == 'he':
        first_line = first_line + " lad "
        first_line = first_line + 'named ' + name
    elif pronoun == 'she':
        first_line = first_line + " lassie "
        first_line = first_line + 'named ' + name
    elif pronoun == 'it':
        first_line = first_line + ", " + r.word(include_parts_of_speech=["adjectives"]) + ' ' + name

    
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

    
    # gerenates all of the lines for the limericks
def generate_limerick(limerick_obj, name, pronoun):
    original_generate_first_line(limerick_obj, name, pronoun)
    original_generate_second_line(limerick_obj, name, pronoun)
    original_generate_3rd_4th_lines(limerick_obj, pronoun)
    original_generate_5th_line(limerick_obj, name, pronoun)





if __name__ == "__main__":

    name = input('Enter who/what will the limerick be about (proper or regular noun): ')
    pronoun = input('Is your object a: He | She | It : ').lower()

    print('\n')

    population = []

    for i in range(POPULATION_SIZE):
        limerick = Limerick(name, pronoun)
        generate_limerick(limerick, name, pronoun)
        population.append(limerick)

    print('initial populaiton of limericks have been created!')

    final_generation = []
    
    for i in range(TOTAL_GENERATIONS):
        print('generation ' + str(i + 1) + ' being computed')
        # below is an arr of limericks in ranked order from the previous generation, highest index is best rank
        ranked_pop = sort_by_rank(population)

        # list of cumulative probabilities based on size of population to select a limerick for recombination
        cumulative_probs = rank_selection_cum_prob_list(len(ranked_pop))

        # below is a list of limericks that will be recombined and potentially mutated
        selected_pop = rank_selection(ranked_pop, cumulative_probs)

        # below is a list of limerickS_IN_POPULATION/2 from recombination and potential mutations
        next_gen = make_next_gen(selected_pop, MUTATION_RATE)

        # Adds the top half from the previous generation to our new recombined and mutated limericks
        middle_index_of_population = int(len(ranked_pop)/2)
        for j in range(middle_index_of_population, len(ranked_pop)):
            next_gen.append(ranked_pop[j])

        population = next_gen
        # if the final genreation has been reached set current generation to final generation
        if i == (TOTAL_GENERATIONS - 1):
            final_generation = next_gen


    best_limerick = None
    best_limerick_fitness = -1000
    for limerick in final_generation:
        total_fitness = syllable_fitness(limerick) + rhyming_fitness(limerick)

        if total_fitness > best_limerick_fitness:
            best_limerick_fitness = total_fitness
            best_limerick = limerick

    print('\n')
    print(best_limerick)
    print('\n')
    print('best_limerick_fitness: ' + str(best_limerick_fitness))







