#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: reducer.py
#description: matrix multiplication Pik=Mij*Njk
#name row cloum value
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-31
#log:

import sys
import re
from itertools import groupby
from operator import itemgetter
#********************-----------------********************#

#********************-----------------********************#
class multiMatrixReduce(object):
    '''
    description: calculate matrix multiplication
    '''
    def __init__(self):
        pass

    def calculate_multip(self):
        all_cont = sys.stdin
        all_cont_list = []
        pattern = re.compile("\w+")
        tmp_list = []
        M_row_group = []
        M_row = []
        M_list = []
        N_colum_group = []
        N_colum = []
        N_list = []
        matrix_result = []
        line_count = 0
        matrix_i = 0
        matrix_j = 0
        matrix_k = 0
        i_j_k = []

        for oneline in all_cont:
            if line_count == 0:
                line_count+=1
                i_j_k = pattern.findall(oneline)
                #print i_j_k
                matrix_i = int(i_j_k[0])
                matrix_j = int(i_j_k[1])
                matrix_k = int(i_j_k[2])
            else:
                tmp_list = pattern.findall(oneline)
                all_cont_list.append(tmp_list)
        for item in all_cont_list:
            if item[0] == "M":
                M_list.append(int(item[3]))
            elif item[0] == "N":
                N_list.append(int(item[3]))
            else:
                print "error!!"
        #把 M 按行分组，方便后面乘法操作
        M_row_group = []
        for i in range(0,matrix_i):#row
            M_row = []
            for j in range(0,matrix_j):#cloum
                M_row.append(M_list[i*matrix_j+j])
            M_row_group.append(M_row)
        #把 N 按列分组，方便后面乘法操作
        N_colum_group = []
        for i in range(0,matrix_k):#colum
            N_colum = []
            for j in range(0,matrix_j):#row
                N_colum.append(N_list[j*matrix_k+i])
            N_colum_group.append(N_colum)
        for i in range(0,matrix_i):
            for j in range(0,matrix_k):
                #获取结果矩阵中的一个值
                sum_value=0
                for (x,y) in zip(M_row_group[i],N_colum_group[j]):
                    sum_value += x*y
                matrix_result.append(sum_value)

            print matrix_result[i*4:i*4+1+j]
        # print i_j_k




if __name__=="__main__":
    mmr = multiMatrixReduce()
    mmr.calculate_multip()
