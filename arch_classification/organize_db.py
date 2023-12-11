# I just organized my database differently and needed to reformat it. I would rather script it than do it manually 

import csv 
import os 

# set directories 
dir_path = os.getcwd() # get current directory , \GeoguesserAutomation\arch_classification
db_path = dir_path+"\\database" # \GeoguesserAutomation\arch_classification\database
train_path = db_path + "\\train" # \GeoguesserAutomation\arch_classification\database\train
test_path = dir_path+"\\test"
csv_train_path = db_path + "\\arch_train_labels.csv"
csv_test_path = db_path + "\\arch_test_labels.csv"

# First, label the images
labels_header = os.listdir(train_path) # [aframe, barndominium, etc]

# find all the labels 
rows=[]
for label in labels_header: # aframe
    label_folder = os.listdir(train_path+"\\" + label) # "C:\dir_path\database\train\aframe"
    for file in label_folder: # 80517-b600.jpg 
        rows.append([file,label]) # ["80517-b600.jpg" , "aframe"]
        os.rename(train_path + "\\" + label+"\\" + file , train_path+"\\"+file) # move the logged file into the train folder 

print(rows)

# write all the labels into a csv 
with open (csv_train_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Filenames","labels"])
    csvwriter.writerows(rows)



# First, label the images
labels_header = os.listdir(test_path) # [aframe, barndominium, etc]

# find all the labels 
rows=[]
for label in labels_header: # aframe
    label_folder = os.listdir(test_path+"\\" + label) # "C:\dir_path\database\train\aframe"
    for file in label_folder: # 80517-b600.jpg 
        rows.append([file,label]) # ["80517-b600.jpg" , "aframe"]
        os.rename(test_path + "\\" + label+"\\" + file , test_path+"\\"+file) # move the logged file into the train folder 

print(rows)

# write all the labels into a csv 
with open (csv_test_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Filenames","labels"])
    csvwriter.writerows(rows)