#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):


    if len(a) == d:
        return a

    #python list slicing makes this super easy!
    newArr = []
    print(str(a[d:len(a)]))
    newArr = a[d:len(a)] + a[0:d] 
    
    return newArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
