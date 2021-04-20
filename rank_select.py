import random
from limerick_class_file import syllable_fitness, rhyming_fitness

'''
This method returns the sum of all the ranks for a given population. It iterates through the size of the
population and sums all the index's. The denominator will be used to calculate probabilities for each
individual index. 
    Params:
        @pop_num {int}: number of individuals within the population
    Return:
        int --> the denominator to be used in rank sum
'''
def ranked_sum(pop_num):
    denominator = 0
    for i in range(1, pop_num + 1):
        denominator += i
    return denominator


'''
This method returns a list with each index filled with probabilities. These probabilities are the sumation of 
all ranks up to the respective index divided by the total sumation of all indexes. For every index, the 
probability is added to the return list creating a list of cumulative proababilites. This list will
be iterated through and checked against a random generated number.
    Params:
        @pop_num {int}: number of individuals within the population
    Return:
        @prob_list {arr[float]}: each index, i, contains the probability of selecting an individual at that index, i, from a ranked population 
'''
def rank_selection_cum_prob_list(pop_num):
    denominator = ranked_sum(pop_num)
    cum_sum = 0
    prob_list = []
    for i in range(1, pop_num+1):
        cum_sum += i
        prob = cum_sum / denominator
        prob_list.append(prob)
    return prob_list


'''
This method takes in the population to be sorted by rank. With this population, another list, pop_rank, is
filled with the corresponding ranks of each individual in the population. These two lists are merged into
one list of tuples that contains individuals and their rank. Rank is based on the two fitness scores summed.
This tuple list is sorted by rank, and a list is returned with the population now ordered by rank with the lowest
rank in the lowest index of the list, and the highest rank in the highest index.
    Params:
        @pop {arr[Limerick obj]}: population of limericks to be sorted by rank
    Return:
        @r {arr[Limerick objs]}: a sorted list of limericks that are ranked by fitness
'''
def sort_by_rank(pop):
    # pop is an array containing our limericks
    pop_rank = []
    for i in range(len(pop)):
        # get the fitness for each limerick of the population
        syllable_fitness_val = syllable_fitness(pop[i])
        rhyming_fitness_val = rhyming_fitness(pop[i])
        limerick_fitness = syllable_fitness_val + rhyming_fitness_val
        pop_rank.append(limerick_fitness)
    # creates list of tuple based on two corresponding lists (index matches index) List of items (limerick OBJECT, fitness)
    fitness = list(zip(pop, pop_rank)) 
    # sorts by fitness
    rank_sorted = sorted(fitness, key=lambda x: x[1]) 
    # returns only string
    r = [individual[0] for individual in rank_sorted] 
    return r


'''
This method takes in the ranked_pop array, which contains the population of limericks sorted by rank. It then
chooses the number of limericks equivalent to the population size (the size of our population) by calling the choose_individual
method. This method returns an array of the population that will now be used for recombination.
    Params:
        @ranked_pop {arr[Limerick objs]}: list of limericks ranked by fitness
        @prob_list {arr[float]}: each index, i, contains the probability of selecting an individual at that index, i, from a ranked population 
    Return:
        @rank_selection_pop {arr[Limerick objs]}: an array of the limericks that will be used for recombination
'''
def rank_selection(ranked_pop, prob_list):
    rank_selection_pop = []
    for i in range(len(ranked_pop)):
        chosen_indiv = choose_individual(ranked_pop, prob_list)
        rank_selection_pop.append(chosen_indiv)

    return rank_selection_pop


'''
This method selects an individual index based of a randomly generated probability. It does so by iterating
throuhg the cumulative probabilites list and cheking if the randomly generated value(between 1-0) is greater
than the current index probability. If it is larger it means that this the individual(limerick) at this index
will be selected for breeding. The cumulative list allows for this itrative process.  
    Params:
        @pop {arr[Limerick obj]}: population of limericks to be sorted by rank
        @prob_list {arr[float]}: each index, i, contains the probability of selecting an individual at that index, i, from a ranked population 
    Return:
        @chosen_indiv {Limerick obj}: the chosen limerick object

'''
def choose_individual(pop, prob_list):
    p = random.uniform(0, 1)
    indiv_index = -99999 #so it doesn't break
    for i in range(len(prob_list)):
        cum_p = prob_list[i]
        #if probability is greater.
        if cum_p >= p: 
            indiv_index = i
            break
    chosen_indiv = pop[indiv_index] #select approprite individual
    return chosen_indiv