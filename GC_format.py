# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:33:52 2022

@author: PRIYANKA
"""


with open ("SENT_calculated_all_no_space.vrt","r", encoding="utf-8") as f_in:
#with open ("sample_calculated_all.vrt","r", encoding="utf-8") as f_in:
    with open ("GC_SENT_calculated_all_no_space.vrt","w", encoding="utf-8") as f_out:
    #with open ("GC_SENT.vrt","w", encoding="utf-8") as f_out:
        for line in f_in:
            line=line.strip("\n")
            line_list=line.split()
            new_line=[]
            list_len=len(line_list)
            if list_len> 4 and line_list[0]!="<text":
                new_line.insert(0,line_list[1])
                new_line.insert(1,line_list[3])
                new_line.insert(2,line_list[0])
                new_line.insert(3,line_list[2])
                
                for i in range(4,len(line_list)):
                    new_line.insert(i,line_list[i])
                print('\t'.join(map(str, new_line)), file=f_out)
                
                
            else: 
                print(line, file=f_out)