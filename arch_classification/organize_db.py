# I just organized my database differently and needed to reformat it. I would rather script it than do it manually 

import csv 
import os 

# set directories 
dir_path = os.getcwd() # get current directory 
db_path = dir_path+"\\database"
train_path = db_path + "\\train"
test_path = dir_path+"\\test"

# First, label the images
labels_header = os.listdir(train_path)

# find all the labels 
rows=[]
for label in labels_header: # each folder in the database
    label_folder = os.listdir(train_path+"\\" + label) # "C:\dir_path\database\train\aframe"
    for file in label_folder: # each file in each folder in the database 
        rows.append([file,label]) # ["file1.jpg" , "aframe"]
        os.rename(train_path + "\\" + label+"\\" + file , train_path+"\\"+file) # move the logged file into the train folder 

# write all the labels into a csv 
with open ("arch_labels.csv", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Filenames","labels"])
    csvwriter.writerow(rows)



