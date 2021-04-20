# imports
from random import randint, sample
from nltk.corpus import words
import random
import pronouncing


'''
This method will determine a line at random from the limerick, determine a random word on that line,
and then replace that word with a newly, randomly generated word.
    Params:
        @limerick_obj {Limerick obj}: the limerick object that will be mutated
    Return:
        None
'''
def mutate_limerick(limerick):
    line_to_mutate = randint(1,5)
    if line_to_mutate == 1:
        line = limerick.line_1 
    elif line_to_mutate == 2:
        line = limerick.line_2
    elif line_to_mutate == 3:
        line = limerick.line_3
    elif line_to_mutate == 4:
        line = limerick.line_4
    else:
        line = limerick.line_5
    
    word_to_mutate = line[randint(1, len(line)) - 1]

    new_word = sample(words.words(), 1)[0]
    phones = pronouncing.phones_for_word(new_word)  

    # makes sure that the word has a definition
    while(len(phones) < 1):
        new_word = sample(words.words(), 1)[0]
        phones = pronouncing.phones_for_word(new_word)

    new_line = line.replace(word_to_mutate, new_word)

    if line_to_mutate == 1:
        limerick.set_line_1(new_line)
    elif line_to_mutate == 2:
        limerick.set_line_2(new_line)
    elif line_to_mutate == 3:
        limerick.set_line_3(new_line)
    elif line_to_mutate == 4:
        limerick.set_line_4(new_line)
    else:
        limerick.set_line_5(new_line)


'''
Creates the first half of the next generation through recombination and mutation. Goes through the parent
generation by two's, after randomly shuffling the parent generation, combing each set of 2 into a new offspring limerick.
   Params:
      @parents {arr[Limerick objs]}: the limericks chosen for recombination from the previous generation
      @mutationRate {float}: the chance that a newly created limerick (from recombination) gets mutated
   Return:
      @next_gen {arr[Limerick objs]}: contains half of the next generation that was created from recombination and (potential) mutation
'''
def make_next_gen(parents, mutationRate):
    #first half of next generation created from recombination will be placed into next_gen
    next_gen = []
    random.shuffle(parents)
    for i in range(0, len(parents), 2):
        mutation = random.uniform(0,1)
        # make a new limerick using crossover
        new_limerick = make_offspring(parents[i], parents[i+1])

        # below if statment triggers mutation
        if (mutation < mutationRate):
            mutate_limerick(new_limerick)

        next_gen.append(new_limerick)

    return next_gen


'''
make_offsrpring preformes crossover. It takes the 3rd and 4th lines from one parent and the 1st, 2nd, and 5th lines from the
other parent. Beacause limericks follow the AABBA rhyme scheme, this type of crossover will not disrupt the rhyming pattern and will
keep the integrity of whatever rhymes the limericks had previously created.
   Params:
      @Parent1 {Limerick obj}: the first limerick parent for the recombination that will occur
      @Parent2 {Limerick obj}: the second limerick parent for the recombination that will occur
   Return:
      Limerick obj --> the limerick obect that has lines 1,2,5 from parents 1 and lines 3,4 from parent 2.
'''
def make_offspring(Parent1, Parent2):
    num = randint(1,2)
    if num == 1:
       line_3 = Parent1.get_line_3()
       line_4 = Parent1.get_line_4()
       Parent2.set_line_3(line_3)
       Parent2.set_line_4(line_4)
       return Parent2
    else:
        line_3 = Parent2.get_line_3()
        line_4 = Parent2.get_line_4()
        Parent1.set_line_3(line_3)
        Parent1.set_line_4(line_4)
        return Parent1
