import numpy as np 
import random
import copy
import math


################################################################################################
#                           One Point Crossover
################################################################################################

def onePointCrossover(sampled_pop, pop_size, cross_rate):

   # cross_rate = 1
    
    pop_values = list(sampled_pop.values())
    np.random.shuffle(pop_values)
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    pop_cross= copy.deepcopy(sampled_pop)
    
    pop_count=0  
    #temp_var=0
    while(pop_count<pop_size and (pop_size-pop_count)>1):

        ind1_rules = sampled_pop[str(pop_count)]['Rules']
        ind2_rules = sampled_pop[str(pop_count+1)]['Rules']
        
        r = random.randint(1,510)
        if(cross_rate>np.random.uniform(0,1)):

            off1_rules = ind1_rules[0:r] + ind2_rules[r:]
            off2_rules = ind2_rules[0:r] + ind1_rules[r:]
            
            pop_cross[str(pop_count)]['Rules'] = off1_rules
            pop_cross[str(pop_count+1)]['Rules'] = off2_rules
        
        #temp_var=pop_count
        pop_count +=2
        
    return pop_cross  


################################################################################################
#                           Uniform Crossover
################################################################################################


def uniformCrossover(sampled_pop, pop_size, cross_rate):  
    
    ##cross_rate= 0.5
    
    # pop_values = list(sampled_pop.values())
    # np.random.shuffle(pop_values)
    # count = 0
    # while(count<pop_size):

    #     sampled_pop[str(count)] = pop_values[count]
    #     count +=1
    
    pop_cross= copy.deepcopy(sampled_pop)
    
    pop_count=0  
    while(pop_count<pop_size and (pop_size-pop_count)>1):
        ind1_rules = sampled_pop[str(pop_count)]['Rules']
        ind2_rules = sampled_pop[str(pop_count+1)]['Rules']
        
        new_rules1=[]
        new_rules2=[]
        
        rule_count =0
        while(rule_count<512):
            ran_value =np.random.uniform(0,1)
            if(ran_value<cross_rate):
                new_rules1.append(ind1_rules[rule_count])
                new_rules2.append(ind2_rules[rule_count])
            else:
                new_rules1.append(ind2_rules[rule_count])
                new_rules2.append(ind1_rules[rule_count])
            
            rule_count+=1
        
        pop_cross[str(pop_count)]['Rules'] = new_rules1
        pop_cross[str(pop_count+1)]['Rules'] = new_rules2
        
        pop_count +=2
    
    return pop_cross 

################################################################################################
#                           N Point Crossover
################################################################################################

def nPointCrossover(sampled_pop, pop_size, cross_rate):  
    
   # cross_rate = 1
    
    n=np.random.randint(150,460)
    pop_values = list(sampled_pop.values())
    np.random.shuffle(pop_values)
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    pop_cross= copy.deepcopy(sampled_pop)
    
    pop_count=0  
    #temp_var=0
    while(pop_count<pop_size and (pop_size-pop_count)>1):

        ind1_rules = sampled_pop[str(pop_count)]['Rules']
        ind2_rules = sampled_pop[str(pop_count+1)]['Rules']
        

        r = random.sample(range(1, 512), n)
        r.sort()
        
        if(cross_rate>np.random.uniform(0,1)):
            
            off1_rules=ind1_rules[0:r[0]]
            off2_rules=ind2_rules[0:r[0]]
            
            k=0;
            while(k<n-1):
                
                if(k%2==0):
                    off1_rules = off1_rules + ind2_rules[r[k]:r[k+1]] 
                    off2_rules = off2_rules + ind1_rules[r[k]:r[k+1]] 
                else:
                    off1_rules = off1_rules + ind1_rules[r[k]:r[k+1]] 
                    off2_rules = off2_rules + ind2_rules[r[k]:r[k+1]] 
                
                k+=1
            
            off1_rules = off1_rules + ind1_rules[r[n-1]:512] 
            off2_rules = off2_rules + ind2_rules[r[n-1]:512] 
                
            
            pop_cross[str(pop_count)]['Rules'] = off1_rules
            pop_cross[str(pop_count+1)]['Rules'] = off2_rules
        
        #temp_var=pop_count
        pop_count +=2
        
        
    
    return pop_cross 