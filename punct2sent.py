# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:43:40 2022

@author: PRIYANKA
"""
path_calculated="/home/pdas/modify_parsed/calculated/"
with open (path_calculated+"calculated_all.vrt","r", encoding="utf-8") as f_in:
    with open ("SENT_calculated_all.vrt","w", encoding="utf-8") as f_out:
        for line in f_in:
            line=line.strip("\n")
            line_list=line.split()
            if len(line_list)> 4:
                if line_list[1]==".":
                    line_list[3]="SENT"
                    line_list[7]="sent"
                    #print(line, file=f_out)
                #else: 
                    #print(line, file=f_out)
                print('\t'.join(map(str, line_list)), file=f_out)
                
                
            else: 
                print(line, file=f_out)
                
