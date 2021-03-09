import numpy as np
import random
import json
import copy
import cv2
from itertools import chain 

import fitnessEvaluation as fit

def binToGrey(current_list):
    
    current_bin=np.where(current_list == 1, 255, current_list) 
    
    return current_bin

def selectNine(row, col, current_array):
    
    #start_image=[[1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    
    current_list = copy.deepcopy(current_array)
    
    #L=len(current_list)
    L_row=len(current_list)
    L_col=len(current_list[0])
    
    if(row<L_row-2):
    
        if(col<L_col-2):
        
            XY= current_list[row:row+3, col:col+3]
            
        elif(col==L_col-2):
        
            x1= current_list[row:row+3, col:col+3]
            x2= current_list[row:row+3, 0:1]
            XY = np.append(x1, x2, axis=1)
            
            
        elif(col==L_col-1):
        
            x1= current_list[row:row+3, col:col+3]
            x2= current_list[row:row+3, 0:2]            
            XY = np.append(x1, x2, axis=1)
                
    elif(row == L_row-2):
    
        if(col<L_col-2):
        
            y1= current_list[row:row+3, col:col+3]            
            y2=current_list[0:1, col:col+3]            
            XY = np.append(y1, y2, axis=0)
            
        elif(col==L_col-2):
            
            x1= current_list[row:row+3, col:col+3]          
            x2= current_list[row:row+3, 0:1]         
            X = np.append(x1, x2, axis=1)
    
            y1=current_list[0:1, col:col+3]        
            y2=current_list[0:1,0:1]
            Y = np.append(y1, y2, axis=1)       
            
            XY = np.append(X, Y, axis=0)
         
            
        elif(col==L_col-1):
        
            x1= current_list[row:row+3, col:col+3]            
            x2= current_list[row:row+3, 0:2]       
            X = np.append(x1, x2, axis=1)
            
            y1=current_list[0:1, col:col+3]          
            y2=current_list[0:1,0:2]                
            Y = np.append(y1, y2, axis=1)  
            
            XY = np.append(X, Y, axis=0)
                   
    elif(row == L_row-1):
    
        if(col<L_col-2):
        
            y1= current_list[row:row+3, col:col+3]        
            y2=current_list[0:2, col:col+3]    
            XY = np.append(y1, y2, axis=0)
       
        elif(col==L_col-2):
            
            x1= current_list[row:row+3, col:col+3]
            x2= current_list[row:row+3, 0:1]        
            X = np.append(x1, x2, axis=1)
                 
            y1=current_list[0:2, col:col+3]    
            y2=current_list[0:2,0:1]                    
            Y = np.append(y1, y2, axis=1)
                  
            XY = np.append(X, Y, axis=0)
  
            
        elif(col==L_col-1):
        
            x1= current_list[row:row+3, col:col+3] 
            x2= current_list[row:row+3, 0:2]
            X = np.append(x1, x2, axis=1)
    
            y1=current_list[0:2, col:col+3]       
            y2=current_list[0:2,0:2]           
            Y = np.append(y1, y2, axis=1)
            
            XY = np.append(X, Y, axis=0)
            
    current_list=XY.tolist()


    flatten_list = list(chain.from_iterable(current_list)) 
    
    return flatten_list

def binaryToDecimal(n): 
    return int(n,2) 

def findRule(individual_rules, current_state):
    
    search = ''.join(map(str, current_state))
    
    dec = binaryToDecimal(search)
    
    ind_list = individual_rules[dec]
    
    current_rule = ind_list[1]
    
    # print("find rule "+str(current_rule)+" current_state "+str(current_state))
    
    return current_rule
            


def operation(current_array, goal_image, ind_rules_table, pop_size, pass_size):
    
    
    #start_image=[[1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    
    #current_array = np.asarray(current_list)
    
    L_row=len(current_array)
    L_col=len(current_array[0])
    
    best_fit = 500000
    #best_arrray = [[0 for x in range(L)] for y in range(L)]
    
    pass_count=0
    while(pass_count<pass_size):
    
        curnt_array_copy =copy.deepcopy(current_array)
        
        row=0
        while (row<L_row):
            col=0
            while(col<L_col):
        
                sub_list9 = selectNine(row, col, current_array)
                
                #print(sub_list9)
                
                rule = findRule(ind_rules_table, sub_list9)
                
                if(row<L_row-1 and col<L_col-1):
                    curnt_array_copy[row+1][col+1]=rule
                    
                elif(row==L_row-1 and col<L_col-1):
                    curnt_array_copy[0][col+1]=rule
                    
                elif(row<L_row-1 and col==L_col-1):
                    curnt_array_copy[row+1][0]=rule
                    
                elif(row==L_row-1 and col==L_col-1):
                    curnt_array_copy[0][0]=rule
                    
                col+=1
                
            row+=1
            
        current_array = copy.deepcopy(curnt_array_copy)
            
        cu_fit_cal = fit.calculate_fitness(curnt_array_copy.astype(np.uint8), goal_image.astype(np.uint8))
                
        if(cu_fit_cal<best_fit):
            best_array=copy.deepcopy(curnt_array_copy)
            best_fit = cu_fit_cal
        
        pass_count += 1
        
    best_array = binToGrey(best_array)
    
    #current_image = copy.deepcopy(current_array)
        
    #current_image = binToGrey(current_image)
    
    #current_image = np.asarray(current_image)
    #goal_image = np.asarray(goal_image)
        
    return best_fit, best_array
            
        
    