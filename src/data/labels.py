import csv
import os

discrete_class = {1 : "0_punching_hole",
                      2 : "1_welding_line",
                      3 : "2_crescent_gap",
                      4 : "3_water_spot",
                      5 : "4_oil_spot",
                      6 : "5_silk_spot",
                      7 : "6_inclusion",
                      8 : "7_rolled_pit",
                      9 : "8_crease",
                      10 : "9_waist_folding"}
    

def general_csv(discrete_class, data_path):
    
    '''Generate a .csv file about the dataset set specify in data_path, with the following structure:
    
    image_id | class | discrete_class'''
    
    with open(data_path+'labels.csv', 'w', newline='') as f:

        writer = csv.writer(f)

        for img_folder in discrete_class:
            for file in os.listdir(os.path.join(data_path+'images/', str(discrete_class[img_folder]))):
                writer.writerow([file, str(discrete_class[img_folder]), str(img_folder-1)])
                
def class_csv(discrete_class, data_path):
    
    '''Generate a .csv file about the class specify in data_path, with the following structure:
    
    image_id | class | discrete_class'''
    
    for img_folder in discrete_class:
    
        with open(data_path+ f'{str(discrete_class[img_folder])}.csv', 'w', newline='') as f:

            writer = csv.writer(f)

            for file in os.listdir(os.path.join(data_path+'images/', str(discrete_class[img_folder]))):
                writer.writerow([file, str(discrete_class[img_folder]), str(img_folder-1)])
                
