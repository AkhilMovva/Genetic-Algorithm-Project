import numpy as np

import collections
import json
import copy



def sortPopulation(population, p_size):
    

    sorted_dic =copy.deepcopy(population)
    values = list(population.values())
    
    sorted_list = sorted(values, key = lambda i: i['fitness']) 
    
    #print(sorted_list)
    
    count = 0
    while(count<p_size):
    
        sorted_dic[str(count)] = sorted_list[count]
        count +=1
        
    #print(sorted_dic)
    
    return sorted_dic










# def sortPop(population, fitVal):
    
#     sorted_pop = [x for _,x in sorted(zip(fitVal,population))]
#     fitVal.sort()
    
#     # population = np.array(population)
#     # fitVal = np.array(fitVal)
#     # inds = fitVal.argsort()
#     # sortedPeople = population[inds]
    
#     # print(fitVal)
#     # print(sortedPeople)
    
#     return sorted_pop, fitVal

# p = [[1,0,1,0,0,0,0,0],[1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
# a = [27, 4, 4, 9]

# sortPop(p, a)
