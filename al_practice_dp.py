#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:28:00 2018

@author: siyanluo
"""

import sys
import time

"""
al_practice_dp.py 

INPUT
12 13
55 92
89 99
64 28
79 46

OUTPUT
12 13 10
55 92 116
89 99 119
28 64 113
46 79 116
('The runtime of this program is', 8.385589122772217)

"""
cycle_length_dic = {'1':1}

def calNumSequence (n):
    lon = [n]
    if cycle_length_dic.get(str(n)) != None:
        return cycle_length_dic[str(n)]
    count = 1
    if n <= 0:
        return 0
    while n != 1:
        if n % 2 == 1:
            n = 3*n + 1
            count = count + 1
            lon.append(n)
        else:
            n = n >> 1
            count = count + 1
            lon.append(n)
    for index in range(0, len(lon)):
        if cycle_length_dic.get(str(lon[index])) == None:
            cycle_length_dic[str(lon[index])] = count - index
        else:
            return index + cycle_length_dic[str(lon[index])]
        
    return -1
        
def accumCycleLength (i, j):
    maxNum = 0
    for num in range (i, j+1):
        if (maxNum < calNumSequence(num)):
            maxNum = calNumSequence(num)
    print("{} {} {}".format(i, j, maxNum))
            
#def main(args):
#    numInput = raw_input()
#    accumCycleLength(list(map(int, numInput.split())))
#
#if __name__ == '__main__':
#    main(sys.argv)
tStart = time.time()#計時開始
for line in sys.stdin:
    curr_line=line.split()
    num1 = int(curr_line[0])
    num2 = int(curr_line[1])
    if num1>num2:
        num1, num2 = num2, num1
    m = accumCycleLength(num1, num2)
tStop = time.time()#計時結束    
print("The runtime of this program is", tStop - tStart)
    