import survivorSelection as disINsurvival
import math

################################################################################################
#                                     Measure Diversity
################################################################################################

def measureDiversity(population, pop_size):
    

    value = 0
    i = 0
    while(i<pop_size):

        ind_puzz1 = population[str(i)]['Rules']
        dis1 = 0
        j=0
        while(j<i):
            
            ind_puzz2 = population[str(j)]['Rules']
            
            d = disINsurvival.distanceFinder(ind_puzz1, ind_puzz2)
            
            dis1 = d + dis1
            
            j+=1
        
        sq = math.sqrt(dis1)
        
        value = sq + value
        
        i+=1
        
    value = value/pop_size
    
    return value