# Genetic-Algorithm-Project
GA for the Cellular Automata

################################################################################################

%%%%%%%%%%%%%%%%%%%%%%%%%        TRAINING       %%%%%%%%%%%%%%%%%%%%%%%%%

We need to run the main file in CellularAutomata/GA1.py

—> For executing this file we need have some libraries like Numpy, cv2, json, matplot, PIL.
—> Here we can adjust different parameters like pop_size, gen_size, mut_rate, cross_rate and no of runs (seed_size) before running.
—> We can also change the initial image by using img_Name and exten_type. And we can also set the bonus here.
—> Defaultly we can run the ALG-1 from the term paper. If you need to run other algorithms we need to uncomment them accordingly.
—> Initial population is stored in CellularAutomata.json

OUTPUT :

—> The each and every generations fitness is printed in the console and images and graphs are plotted.
—> The best CA rule table is stored in best_rules_table.json file. And the start, goal and final images are stored in the out_images folder.


%%%%%%%%%%%%%%%%%%%%%%%%%         TESTING        %%%%%%%%%%%%%%%%%%%%%%%%%

We need to run the main file in CellularAutomata/checking_edge_detect.py

—> All the images which I’m going to test are present in the same CellularAutomata folder.
—> We can also add any other images of different sizes to test. But the images should be given in the format mentioned in the code for a 
Convenient output.
—> We can directly test with the rule table of different algorithms  which I stored in Results folder. Where we just need to directly copy the 
best_rules_table.json file to the CellularAutomata folder where the codes are present.

OUTPUT :

—> We can see the results like image_name, fitness, SSIM values in the console. And the images are stored in the check_images folder.

%%%%%%%%%%%%%%%%%%%%%%%%%        OTHER       %%%%%%%%%%%%%%%%%%%%%%%%%%%

—> All the functions are stored in their respective files in the CellularAutomata folder.
—> We can also see Results folder where I have presented ALG-1 and MoALG-1 outputs in their respective folders.
       —> Each folder having its images along with rule table json file and data file. 
       —> Data file contains the RUNS, Generations and fitness values.

################################################################################################
