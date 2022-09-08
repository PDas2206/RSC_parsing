# -*- coding: utf-8 -*-
"""
Created on Tue May 24 02:31:14 2022

@author: PRIYANKA
"""


def remove_blank_lines(file_name):
    line_list=[]
    with open(file_name, 'r',encoding="utf-8") as f:
        with open("SENT_calculated_all_no_space.vrt", 'w', encoding="utf-8") as f_nospace:
            for line in f:
                line=line.strip("\n")
                line_list=line.split()
                if line !='':
                    if line_list[0]=="#" and line_list[1]=="newdoc":
                        print("</text>", file=f_nospace)
                    if line_list[0]!="#":
                        '''
                        if line_list[1]=='.':
                            line_list[3]='SENT'
                            print(listToString(line_list,'\t')[:-1], file=f_nospace)
                        '''
                        print(line, file=f_nospace)
                #if line_list[0]!="#" or line!='':
                 #   print(line,  file=f_nospace)             
                    #print("".join(line if not line.isspace()), file=f_nospace)
        
remove_blank_lines("SENT_calculated_all.vrt")
#remove_blank_lines("sample.txt")                    


                    


