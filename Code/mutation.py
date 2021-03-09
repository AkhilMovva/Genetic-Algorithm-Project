import random
import numpy as np
import copy
import math

################################################################################################
#                                Uniform Mutation
################################################################################################

def mutation(crossedPopulation, mut_rate, pop_size):
    
    mutatedPopulation = copy.deepcopy(crossedPopulation)
    pop_count = 0
    while(pop_count<pop_size):
        ind = key, val = random.choice(list(crossedPopulation.items()))
        
        ind_rules =ind[1]['Rules']
        new_rules=[]
        for r in ind_rules:    
            changed = False      
            ran_value =np.random.uniform(0,1)
            if(mut_rate>ran_value):
                r[1]=np.random.randint(2)
                changed=True
                new_rules.append(r)
            if not(changed):
                new_rules.append(r)
        
        mutatedPopulation[str(ind[0])]['Rules']=new_rules
        
        pop_count +=1
        
        return mutatedPopulation