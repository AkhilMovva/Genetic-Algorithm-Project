import cv2
import json
import numpy as np
from PIL import Image 
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim

import operations as opt
 

def view_image(image, name,img_NAME):
    img = Image.fromarray(np.uint8(image))

    img.save("check_images/"+img_NAME+'_'+name+".png")

def view_image2(image, name, img_NAME, fitness):
    img = Image.fromarray(np.uint8(image))

    img.save("check_images/"+img_NAME+'_'+name+'_'+str(fitness)+".png")
    
def greyToBin(current_list):   
    current_bin=np.where(current_list==255, 1, current_list) 
    return current_bin


def edge_detection(initial_image,img_NAME, binary):
    
    if(binary == False):
        for x_pixel in range(len(initial_image)):
          for y_pixel in range(len(initial_image[0])):
            if initial_image[x_pixel][y_pixel] < 128:
              initial_image[x_pixel][y_pixel] = 0
            elif initial_image[x_pixel][y_pixel] >= 128:
              initial_image[x_pixel][y_pixel] = 255
        
        goal_image = cv2.Canny(initial_image, len(initial_image), len(initial_image[0]))
    elif(binary == True):
        start_image = initial_image
        goal_image = cv2.Canny(initial_image, len(initial_image), len(initial_image[0]))
    
    
    start_image = initial_image
    goal_image = goal_image
    
    view_image(start_image, "Start_Image", img_NAME)
    view_image(goal_image, "Goal_Image", img_NAME)
    
    with open("best_rules_table.json",'r') as f:
      rule_table = json.loads(f.read());
      
    
    start_image_bin = greyToBin(start_image)
    goal_image_bin = greyToBin(goal_image)
    
        
    fit_cal, final_image= opt.operation(start_image_bin, goal_image_bin, rule_table, pop_size=1, pass_size=1)
    
    
    view_image2(final_image, "final_Image",img_NAME, fit_cal)
    
    print(img_name+" - Fitness : "+str(fit_cal))
    
    ssim_value = ssim(final_image, goal_image)
    
    print(img_name+" - SSIM : "+str(ssim_value))
    
    with open("check_images/best_rules_table.json", 'w') as o:
        o.write(json.dumps(rule_table))
    
    
 
    
    
img_name="shapes"
edge_detection(cv2.imread(img_name+".jpg", 0), img_name, binary=False)
img_name="mixed"
edge_detection(cv2.imread(img_name+".jpg", 0), img_name, binary=False)
img_name="cells"
edge_detection(cv2.imread(img_name+".png", 0), img_name, binary=False)
img_name="binaryhand"
edge_detection(cv2.imread(img_name+".png", 0), "hand", binary=True)
img_name="apple"
edge_detection(cv2.imread(img_name+".jpeg", 0), img_name, binary=False)
img_name="parts"
edge_detection(cv2.imread(img_name+".png", 0), img_name, binary=False)
img_name="lena"
edge_detection(cv2.imread(img_name+".tif", 0), img_name, binary=False)
img_name="hand_Start_Image_0"
edge_detection(cv2.imread(img_name+".png", 0), "hand1", binary=True)
img_name="hand_Start_Image_1"
edge_detection(cv2.imread(img_name+".png", 0), "hand2", binary=True)
img_name="hand_Start_Image_2"
edge_detection(cv2.imread(img_name+".png", 0), "hand3", binary=True)
img_name="hand_Start_Image_3"
edge_detection(cv2.imread(img_name+".png", 0), "hand4", binary=True)
img_name="hand_Start_Image_4"
edge_detection(cv2.imread(img_name+".png", 0), "hand5", binary=True)



