#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: mapper.py
#description: matrix multiplication Pik=Mij*Njk
#file form:
# M
# i j
# x y z
# ...
# N
# j K
# a b c d
# ....
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-31
#log:


import sys
import re
import pdb
#********************-----------------********************#

#********************-----------------********************#
class multiMatrixMap(object):
    '''
        description: map matrix into element and groupby M_row and N_cloum
    '''

    def __init__(self):
        pass

#-----------------********************-----------------#
    def generate_map_output(self):
        '''
            description: generate map output content
            input:
                none
            output:
                map output content
        '''
        # fd = open("./data.txt",'r')
        # all_cont = fd.readlines()
        all_cont = sys.stdin
        matrix_name_P = re.compile("\w+")
        matrix_name = []
        matrix_row_colum_P = re.compile("\d+")
        matrix_row_colum = []
        matrix_value_P = re.compile("\d+")
        matrix_value_row = []
        output_string_list = []
        over_line_num = 0
        line_count = 0
        row_num = 0
        colum_num = 0
        row_colum_list = []
        # print all_cont
        for oneline in all_cont:
            if line_count == 0:
                line_count += 1
                matrix_name = []
                matrix_name = matrix_name_P.findall(oneline)
                # print matrix_name
            elif line_count == 1:
                line_count += 1
                over_line_num=2
                matrix_row_colum = []
                for item in matrix_row_colum_P.findall(oneline):
                    matrix_row_colum.append(int(item))
                # print matrix_row_colum
                # print "@@@"
                row_num = matrix_row_colum[0]
                colum_num = matrix_row_colum[1]
                row_colum_list.append(row_num)
                row_colum_list.append(colum_num)
            else:
                line_count += 1
                if line_count <= (over_line_num+row_num):
                    #reset
                    matrix_value_row = []
                    for item in matrix_value_P.findall(oneline):
                        matrix_value_row.append(int(item))
                    for i in range(0,len(matrix_value_row)):
                        output_string_list.append(matrix_name[0]+" %d %d %d"%((line_count-over_line_num-1), i, matrix_value_row[i]))
                else:
                    line_count = 1
                    matrix_name = []
                    matrix_name = matrix_name_P.findall(oneline)
                    # print matrix_name
                    # print "###"
        print "%d  %d  %d"%(row_colum_list[0], row_colum_list[1], row_colum_list[3])
        for item in output_string_list:
            print item


if __name__=="__main__":
    mm_tmp = multiMatrixMap()
    mm_tmp.generate_map_output()
