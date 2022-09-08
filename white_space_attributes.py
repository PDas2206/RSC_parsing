# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:10:27 2022

@author: PRIYANKA
"""

with open ("GC_SENT_calculated_all_no_space.vrt","r", encoding="utf-8") as f_in:

    with open ("GC_final.vrt","w", encoding="utf-8") as f_out:
    
        for line in f_in:
            line=line.strip("\n")
            line_list=line.split()
            
            
            if line_list[0]=="<text" or line_list[0]=="<s":
                
                print(' '.join(map(str, line_list)), file=f_out)
                
                
            else: 
                print(line, file=f_out)
