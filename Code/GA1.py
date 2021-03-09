import numpy as np
import json
import cv2
import copy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.pyplot import show, plot
from PIL import Image 
import statistics

################################################################################################
#                                   Name: Akhil Movva                                          #
#                                     ID: 40106477                                             #
#                                CELLULAR AUTOMATA PROJECT                                     #
################################################################################################

import initializePopulation as iniPop
import operations as opt
import sortPopulation as sort

import parentSelection as parSel
import crossover as cros
import mutation as mut
import survivorSelection as surSel
import fitnessEvaluation as fit
import diversity as div

pop_size = 50
gen_size = 50
pass_size = 1
seed_size = 3
mut_rate = 0.2
cross_rate = 0.8

img_NAME ="binaryhand"
exten_type = ".png"
initial_image = cv2.imread(img_NAME+exten_type, 0)
bonus = False

def greyToBin(current_list):   
    current_bin=np.where(current_list==255, 1, current_list) 
    return current_bin

def view_image(image, name):
    img = Image.fromarray(np.uint8(image))

    img.save("out_images/"+name+".png")

    #img.show()


def visualize_image(image):
  # cv2.imshow('',image)
  # cv2.waitKey(0)
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    show(block=False)
    
    
def print_population(population_json):
  json_obj = json.loads(population_json)
  
def cal_operation(start_image, goal_image, population_rules):
    
    modified_population={}
    
    start_image_bin = greyToBin(start_image)
    goal_image_bin = greyToBin(goal_image)
    
    for i in range (pop_size):
        
        fit_cal, modified_image= opt.operation(start_image_bin, goal_image_bin, population_rules[i], pop_size, pass_size)
    
        modified_population[str(i)] = {"fitness": fit_cal, "Rules": population_rules[i],"final image": modified_image}
    
    return modified_population

def get_ind_Rules(pop_dic):
    
    ind_pop_rules=[]
    
    for key in pop_dic:
        ind_pop_rules.append(pop_dic[key]["Rules"])
    
    return ind_pop_rules
  
################################################################################################
#                                      MAIN PROGRAM
################################################################################################
    
fit_max_seed_avg = np.zeros(gen_size)
fit_mean_seed_avg = np.zeros(gen_size)

initial_div = []
final_div = []  

#initial_image = cv2.imread("mixed.jpg", 0)
#visualize_image(initial_image) 
#view_image(initial_image)
best_fit = 500000

for s in range(seed_size):
    
    

    iniPop.initialize_population(initial_image, pop_size, bonus)
    
    with open("CellularAutomata.json",'r') as f:
      population = json.loads(f.read());
    
    
    start_image = np.asarray(population[0])
    goal_image = np.asarray(population[1])
    
    # start_image = initial_image
    # goal_image = cv2.Canny(initial_image, 256, 256)
      
    visualize_image(start_image)
    visualize_image(goal_image)  
    view_image(start_image, img_NAME+"_"+"Start_Image"+"_"+str(s))
    view_image(goal_image, img_NAME+"_"+"Goal_Image"+"_"+str(s))
    
    population_rules = population[2:]
    
    main_Pop = cal_operation(start_image, goal_image, population_rules) 
    print("Random Initial Population's best fitness - "+str(main_Pop[str(0)]["fitness"]))
    visualize_image(main_Pop[str(0)]["final image"]) 
    
    initial_div.append(div.measureDiversity(main_Pop, pop_size))
    
    fit_max_gen = []
    fit_mean_gen = []

    fit_std_gen = []
    
    gen_count= 0
    
    while(gen_count<gen_size):
        
        all_fit_gen = []
        
        sortedPop = copy.deepcopy(sort.sortPopulation(main_Pop, pop_size))
        sortedPop2 = copy.deepcopy(sortedPop)
        
        ###***************************** Parent Selection *****************************###
        selectedPop = copy.deepcopy(parSel.uniformParentSelection(sortedPop, pop_size))
        # selectedPop = copy.deepcopy(parSel.expParentSelection(sortedPop, pop_size))
        # selectedPop = copy.deepcopy(parSel.fitnessbasedParentSelection(sortedPop, pop_size))
        
        ###*****************************     Crossover    *****************************###
        #crossedPop = cros.onePointCrossover(selectedPop, pop_size, cross_rate)
        
        crossedPop = cros.uniformCrossover(selectedPop, pop_size, cross_rate)
        
        #crossedPop = cros.nPointCrossover(selectedPop, pop_size, cross_rate)
        # ind_cross_rules = get_ind_Rules(crossedPop)
        # updatedPopulationFitness1 =cal_operation(start_image, goal_image, ind_cross_rules)
        
        
        mu = mut_rate
                           
        # if( gen_count > round(gen_size//2)):
        #     res = fit_max_gen[-10:]
        #     set_res = set(res)
        #     if(len(set_res)<4):
        #         mu = 0.4
        
        
        ###*****************************     Mutation      *****************************###
        mutatedPop=mut.mutation(crossedPop, mu, pop_size)
        
        
        ind_mut_rules = get_ind_Rules(mutatedPop)
        updatedPopulationFitness2 =cal_operation(start_image, goal_image, ind_mut_rules)
        
        ###***************************** Survival Selection *****************************###
        survivalPop = surSel.survivorSelONFitness(sortedPop2, updatedPopulationFitness2, pop_size)
        # survivalPop = surSel.survivorSelONCrowding(sortedPop2, updatedPopulationFitness2, pop_size)

        
        main_Pop=copy.deepcopy(survivalPop)
        
        visualize_image(survivalPop[str(0)]["final image"]) 
        #view_image(survivalPop[str(0)]["final image"],str(s)+"_"+str(gen_count)) 

        
        fit_max_gen.append(survivalPop["0"]['fitness'])
        fit_mean_gen.append((sum(d['fitness'] for d in survivalPop.values() if d))/pop_size )
        
        for k in survivalPop.values():
            all_fit_gen.append(k['fitness'])
        fit_std_gen.append(np.std(all_fit_gen))


        
        print(" SEED " + str(s)+" GEN " + str(gen_count)+" fitness : "+" = "+str(survivalPop["0"]['fitness']))
        
        gen_count+=1
    
    cu_fit_cal=main_Pop["0"]['fitness']
    if(cu_fit_cal<best_fit):
        best_fit = cu_fit_cal   
        with open("best_rules_table.json", 'w') as o:
            o.write(json.dumps(main_Pop[str(0)]["Rules"]))
        
        
    x_axis = np.arange(0, gen_size).tolist()
    plt.figure()
    plt.plot(x_axis, fit_max_gen)
    plt.legend(['max s per gen'])
    
    plt.figure()
    plt.plot(x_axis, fit_mean_gen)
    plt.legend(['avg s per gen'])
        
    plt.figure()
    plt.plot(x_axis, fit_std_gen)
    plt.legend(['std s per gen'])
    
    
    fit_max_seed_avg = np.vstack((fit_max_seed_avg, fit_max_gen))
    fit_mean_seed_avg  = np.vstack((fit_mean_seed_avg, fit_mean_gen))
    
    final_div.append(div.measureDiversity(survivalPop, pop_size))
    view_image(main_Pop[str(0)]["final image"], img_NAME+"_"+"Final_Image"+"_"+str(s))

#print(main_Pop[str(0)]["fitness"])
visualize_image(main_Pop[str(0)]["final image"]) 


fit_max_seed_avg = np.delete(fit_max_seed_avg, (0), axis=0)
fit_max_seed_mean=fit_max_seed_avg.mean(axis=0)
fit_max_seed_std=fit_max_seed_avg.std(axis=0)

fit_mean_seed_avg = np.delete(fit_mean_seed_avg, (0), axis=0)
fit_mean_seed_mean=fit_mean_seed_avg.mean(axis=0)
fit_mean_seed_std=fit_mean_seed_avg.std(axis=0)
       
x_axis = np.arange(0, gen_size).tolist()
plt.figure()
plt.plot(x_axis, fit_max_seed_mean)
plt.legend(['max s mean per gen'])

plt.figure()
plt.plot(x_axis, fit_max_seed_std)
plt.legend(['max s std per gen'])

plt.figure()
plt.plot(x_axis, fit_mean_seed_mean)
plt.legend(['avg s mean per gen'])

plt.figure()
plt.plot(x_axis, fit_mean_seed_std)
plt.legend(['avg s std per gen'])

#print(fit_max_gen)
#print(final_states_list)

print("initial_div "+str(initial_div)+" final_div "+str(final_div))
