#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import math
import os
import random
import re
import sys
# Complete the isValid function below.
def isValid(s):
    # valid if all characters of the string appear the same number of times.       It is also valid if he can remove just 1 character at  1 index in the    string, and the remaining characters will occur the same number of times. 

    # make a dictionary with keys as each character in given string
    d = dict.fromkeys(list(s), 0)

    # fill dictionary with letter count for each letter in given string
    for char in s:
        d[char] += 1
    print(d)

    # there can only be two values. if there is more than one value, increment.
    # if the second of these two values occurs more than once, return 'NO'
    moreThanOne = 0

    #first value in dict
    okVal = next(iter(d.values()))


    for key in d:
        if d[key] != okVal:
            moreThanOne += 1

        if moreThanOne > 1:
          return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
