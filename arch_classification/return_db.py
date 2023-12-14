# putting images back into their rightful folders for vgg

import csv 
import os 

# set directories 
dir_path = os.getcwd() # get current directory , \GeoguesserAutomation\arch_classification
db_path = dir_path+"\\database\\" # \GeoguesserAutomation\arch_classification\database
train_path = db_path + "train\\" # \GeoguesserAutomation\arch_classification\database\train
valid_path = db_path+"valid\\"
csv_train_path = db_path + "arch_train_labels.csv"
csv_valid_path = db_path + "arch_valid_labels.csv"


# read each img in csv and put back into folder of same name 
with open (csv_train_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        if not (row[0] == 'Filenames'):
            try:
                print(row)
                os.rename(train_path + row[0], train_path + row[1] + "\\" + row[0])
            except:
                print("moving on")


with open (csv_valid_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        if not (row[0] == 'Filenames'):
            try: 
                print(row)
                os.rename(valid_path + row[0], valid_path + row[1] + "\\" + row[0])
            except:
                print("moving on")