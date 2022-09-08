# -*- coding: utf-8 -*-
"""
Created on Wed May 18 02:37:06 2022

@author: PRIYANKA
"""
import os

def adding_metadata(file_source, file_modified, path_modified, path_source):
    '''This will add the metadata'''
    #path = "C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/source/"
    
    with open(path_source+file_source, 'r', encoding="utf-8") as f_source:
        with open(path_modified+file_modified,'w', encoding="utf-8") as f_modified:
            metadata = f_source.readline()
            print(metadata,file=f_modified)
    

def modify(file_target, file_modified, path_modified, path_target):
    '''This will modify the target files'''
    #path = "C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/target/"
    line_list=[]
    with open(path_target+file_target, 'r', encoding="utf-8") as f_target:
        with open(path_modified+file_modified,'a', encoding="utf-8") as f_modified:
            for line in f_target:
                line=line.strip("\n")
                line_list=line.split()
                if line =='':
                    print("</s>", file=f_modified)
                    
                
                elif line_list[0]=="#" and line_list[1]=="sent_id":
                    sent_tag="<s "+"sent_id = "+str(line_list[3])+">"
                    print(sent_tag, file=f_modified)
                    
                else: 
                    print(line, file=f_modified)
                
                

def retrieving_target_files(path_target):
    '''This returns a list of all the files in the TARGET folder'''
    # The path for the folder containing the target files (conllu)
    #path = "C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/target/"
    list_of_target_files = os.listdir(path_target)
    
       
    # To retrieve only the name of the files without the extension
    for i in range(len(list_of_target_files)): 
        list_of_target_files[i]=list_of_target_files[i].rsplit('.', 1)[0] 
    return list_of_target_files

def retrieving_source_files(path_source): 
    '''This returns a list of all the files in the SOURCE folder'''
    # The path for the folder containing the source files (vrt)
    #path = "C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/source/"
    list_of_source_files = os.listdir(path_source)
    
    # To retrieve only the name of the files without the extension
    for i in range(len(list_of_source_files)): 
        list_of_source_files[i]=list_of_source_files[i].rsplit('.', 1)[0] 
    return list_of_source_files
          
      
def finding_matching_source_files(target_file, list_of_source_files):
    '''This will find the corresponding target file acc to the source file name'''
    c=0
    for source_file in list_of_source_files:
        if target_file==source_file:
            c+=1
            source_file=str(source_file)+".vrt"
            print("working on file",source_file)
            return source_file
    if c==0:
        
        return "x"
            
    
                    
    


def selecting_target_files(list_of_target_files, list_of_source_files, path_modified, path_target, path_source):
    '''For each target file in the TARGET folder, this function finds its matching source file from the SOURCE folder'''
    for target_file in list_of_target_files:
        file_source=finding_matching_source_files(target_file, list_of_source_files)
        if file_source=="x":
            print("No file found for the target file",target_file,"in the source file list")
        else:
            file_modified=str(target_file)+".txt"
            file_target=str(target_file)+".conllu"
                
            adding_metadata(file_source, file_modified, path_modified, path_source)
            modify(file_target, file_modified, path_modified, path_target)
        






'''path to store the new modified target files'''
path_modified="/home/pdas/modify_parsed/modified/"
#path_modified="C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/modified/"

'''path to retrieve the source files'''
path_source="/home/pdas/modify_parsed/src/"
#path_source = "C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/source/"

'''path to retrieve the target files'''
path_target="/home/pdas/modify_parsed/all_conllu/"
#path_target = "C:/Users/PRIYANKA/Desktop/Language Science and Technology/Uni B1/Modifying Parsed files/target/"


list_of_target_files=retrieving_target_files(path_target)
list_of_source_files=retrieving_source_files(path_source)
selecting_target_files(list_of_target_files, list_of_source_files, path_modified, path_target, path_source)


