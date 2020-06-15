import os
import shutil
import random
import math

classes = ['cat', 'dog']

#Function for creating the directories of different classes 
#Takes train, test or valid as input
def create_dir(dir_name):
    if os.path.isdir(dir_name) is False: 
        print("creating", dir_name)
        os.mkdir( # YOUR ABSOLUTE DIR PATHN WHERE YOU WANT TO CREATE THIS DIRECTORY # + '\\' + dir_name)
        os.chdir(dir_name)
        for i in classes:
            os.mkdir(f'{i}')
        print(dir_name, "created!")
        os.chdir('..')
    else:
        print(dir_name, "already exists!")

#Function to get list of files in a directory
def get_list_files(dir_path):
    list_files = next(os.walk(dir_path))[2] #dir_path is your directory path as string
    return list_files

#Function to copy images from datasets to relevant directories acc. to given test, train and valid ratios
def dataset_to_dir(dataset_dir, dir_class, target_dir, train_ratio, test_ratio, valid_ratio):
    if (train_ratio + test_ratio + valid_ratio > 1):
        print("Invalid Ratios!")
    else:
        dataset_dir = dataset_dir + '\\' + dir_class
        list_files = get_list_files(dataset_dir)
        total_num_files = len(list_files)
        counter = 0
                
        num_files_to_transfer_to_train = math.floor(total_num_files * train_ratio)
        num_files_to_transfer_to_test = math.floor(total_num_files * test_ratio)
        num_files_to_transfer_to_valid = math.floor(total_num_files * valid_ratio)
        
        for i in range(total_num_files):
            #Transfering file to Train Acc. to given Ratio
            if  (counter > 0 and counter < num_files_to_transfer_to_train):                
                src = dataset_dir + '\\' + list_files[counter] 
                dest = target_dir + f'\\train\\{dir_class}\\' + list_files[counter]
                shutil.copyfile(src, dest)
                counter += 1
            
            #Transfering file to Test Acc. to given Ratio
            elif (counter > num_files_to_transfer_to_train and \
                  counter <= num_files_to_transfer_to_train + num_files_to_transfer_to_test):                
                src = dataset_dir + '\\' + list_files[counter] 
                dest = target_dir + f'\\test\\{dir_class}\\' + list_files[counter]
                shutil.copyfile(src, dest)
                counter += 1
                
            #Transfering file to Valid Acc. to given Ratio                
            else:                
                src = dataset_dir + '\\' + list_files[counter] 
                dest = target_dir + f'\\valid\\{dir_class}\\' + list_files[counter]
                shutil.copyfile(src, dest)
                counter += 1

#Creating the directories
parent_dir = # YOUR ABSOLUTE DIR PATHN WHERE YOU'RE WORKING #
os.chdir(parent_dir)
create_dir("train")
create_dir("test")
create_dir("valid")

#Calling the function for all classes
#NOTE: train_split + valid_split + test_split <= 1
train_split = # your train split #
valid_split = # your valid split #
test_split  = # your test split # 

for i in classes: 
    dataset_to_dir(parent_dir + '\\' + 'Image Data',
                   f"{i}",
                   parent_dir,
                   train_split, test_split, valid_split)









