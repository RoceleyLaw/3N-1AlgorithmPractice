#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 04:16:49 2018

@author: siyanluo
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:28:00 2018

@author: siyanluo
"""

import sys
import time

"""
al_practice_original

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
('The runtime of this program is', 2.7199718952178955)
"""

def calNumSequence (n):
    count = 1
    if n <= 0:
        return 0
    while n != 1:
        if n % 2 == 1:
            n = 3*n + 1
            count = count + 1
        else:
            n = n >> 1
            count = count + 1
    return count
        
def accumCycleLength (i, j):
#    list_cycle_length = [0]
    maxNum = 0
    for num in range (i, j+1):
        #print("this is the num", num)
        if (maxNum < calNumSequence(num)):
            maxNum = calNumSequence(num)
#        list_cycle_length.append(calNumSequence(num))
    print("{} {} {}".format(num1, num2, maxNum))
            
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
    