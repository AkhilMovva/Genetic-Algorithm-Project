import math
import numpy as np
import random
import copy
import collections
import sortPopulation as sort


################################################################################################
#                            Survival Selection Based on Top Fitness vales
################################################################################################
    

def survivorSelONFitness(parents_pop, offspring_pop, pop_size):
    
    count = 0
    temp_parent_pop = copy.deepcopy(parents_pop)
    temp_parent_pop = sort.sortPopulation(temp_parent_pop, pop_size)
    temp_pop = sort.sortPopulation(offspring_pop, pop_size)
    temp_pop = copy.deepcopy(offspring_pop)
    while(count<pop_size):

        p = list(temp_pop.keys())[count]

        offspring_pop[str(pop_size+count)] = offspring_pop.pop(str(p))
    
        count +=1
    
    parents_pop.update(offspring_pop)
    sorted_pop = sort.sortPopulation(parents_pop, 2*pop_size)
    # print(parents_pop)
    # res1 = dict(list(parents_pop.items())[pop_size:]) 
    res = dict(list(sorted_pop.items())[:pop_size]) 

    
    return res
################################################################################################
#                            Survival Selection Based on Crowding
################################################################################################
    

def euclideanDis(point1, point2):
    
    return ((((point1-point2)**2))**0.5)

def distanceFinder(rule1, rule2):

    points1=[]
    points2=[]
    dis_var=0
    
    count=0
    while(count<512):
        l=rule1[count][1]
        points1.append(l)
        count+=1
    count=0
    while(count<512):
        b=rule2[count][1]
        points2.append(b)
        count+=1
    
    count=0
    while(count<512):
        dis_cal = euclideanDis(points1[count], points2[count])
        dis_var = dis_var + dis_cal
        
        count+=1
    
    return dis_var

def survivorSelONCrowding(parents_pop, offsprings_pop, pop_size):
    
    temp1 = copy.deepcopy(parents_pop)
    temp2 = copy.deepcopy(offsprings_pop)
    
    survivor_pop = copy.deepcopy(parents_pop)
    
    #pieces = parents_pop[str(0)]['Rules']
    
    parent_pop_values = list(temp1.values())
    np.random.shuffle(parent_pop_values)
    count = 0
    while(count<pop_size):

        temp1[str(count)] = parent_pop_values[count]
        count +=1
    
    parents_pop= copy.deepcopy(temp1)
    
    offsprings_pop_values = list(temp2.values())
    np.random.shuffle(offsprings_pop_values)
    count = 0
    while(count<pop_size):

        temp2[str(count)] = offsprings_pop_values[count]
        count +=1
    
    offsprings_pop= copy.deepcopy(temp2)
    
    pop_count = 0
    while(pop_count<pop_size):

        parent1_puzzle = parents_pop[str(pop_count)]['Rules']
        parent2_puzzle = parents_pop[str(pop_count+1)]['Rules']
        parent1_fitness = parents_pop[str(pop_count)]['fitness']
        parent2_fitness = parents_pop[str(pop_count+1)]['fitness']
                                       
        offspring1_puzzle = offsprings_pop[str(pop_count)]['Rules']
        offspring2_puzzle = offsprings_pop[str(pop_count+1)]['Rules']
        offspring1_fitness = offsprings_pop[str(pop_count)]['fitness']
        offspring2_fitness = offsprings_pop[str(pop_count+1)]['fitness']
        
        direct_dis1 = distanceFinder(parent1_puzzle, offspring1_puzzle)
        direct_dis2 = distanceFinder(parent2_puzzle, offspring2_puzzle)
        
        cross_dis1 = distanceFinder(parent1_puzzle, offspring2_puzzle)
        cross_dis2 = distanceFinder(parent2_puzzle, offspring1_puzzle)

        if((direct_dis1+direct_dis2)<(cross_dis1+cross_dis2)):
            
            if(parent1_fitness>offspring1_fitness):              
                # survivor_pop[str(pop_count)]['Rules']= offsprings_pop[str(pop_count)]['Rules']
                # survivor_pop[str(pop_count)]['fitness'] = offspring1_fitness
                survivor_pop[str(pop_count)]= offsprings_pop[str(pop_count)]
            
            else:               
                # survivor_pop[str(pop_count)]['Rules']= parents_pop[str(pop_count)]['Rules']
                # survivor_pop[str(pop_count)]['fitness'] = parent1_fitness
                survivor_pop[str(pop_count)]= parents_pop[str(pop_count)]
                                       
            if(parent2_fitness>offspring2_fitness):              
                # survivor_pop[str(pop_count+1)]['Rules']= offsprings_pop[str(pop_count+1)]['Rules']
                # survivor_pop[str(pop_count+1)]['fitness'] = offspring2_fitness
                survivor_pop[str(pop_count+1)]= offsprings_pop[str(pop_count+1)]
            
            else:                
                # survivor_pop[str(pop_count+1)]['Rules']= parents_pop[str(pop_count+1)]['Rules']
                # survivor_pop[str(pop_count+1)]['fitness'] = parent2_fitness
                survivor_pop[str(pop_count+1)]= parents_pop[str(pop_count+1)]
                
            
        else:
            if(parent1_fitness>offspring2_fitness):              
                # survivor_pop[str(pop_count)]['Rules']= offsprings_pop[str(pop_count+1)]['Rules']
                # survivor_pop[str(pop_count)]['fitness'] = offspring2_fitness
                survivor_pop[str(pop_count)]= offsprings_pop[str(pop_count+1)]
            
            else:               
                # survivor_pop[str(pop_count)]['Rules']= parents_pop[str(pop_count)]['Rules']
                # survivor_pop[str(pop_count)]['fitness'] = parent1_fitness
                survivor_pop[str(pop_count)]= parents_pop[str(pop_count)]
                                       
            if(parent2_fitness>offspring1_fitness):              
                # survivor_pop[str(pop_count+1)]['Rules']= offsprings_pop[str(pop_count)]['Rules']
                # survivor_pop[str(pop_count+1)]['fitness'] = offspring1_fitness
                survivor_pop[str(pop_count+1)]= offsprings_pop[str(pop_count)]
            
            else:                
                # survivor_pop[str(pop_count+1)]['Rules']= parents_pop[str(pop_count+1)]['Rules']
                # survivor_pop[str(pop_count+1)]['fitness'] = parent2_fitness
                survivor_pop[str(pop_count+1)]= parents_pop[str(pop_count+1)]
               
        pop_count +=2 
        
        survivalPop = copy.deepcopy(sort.sortPopulation(survivor_pop, pop_size))
    
    return survivalPop

