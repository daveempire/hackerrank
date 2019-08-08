#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

import string
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    deletions = 0

    # sets keys of dictionary equal to a-z with values of 0
    aDict = dict.fromkeys(string.ascii_lowercase, 0)
    bDict = dict.fromkeys(string.ascii_lowercase, 0)

    # fill dictionary a
    for x in a:
        aDict[x] += 1

    # fill dictionary b
    for x in b:
        bDict[x] += 1

    # for letter count in alphabet, compare value at each letter in both dicts
    for x in aDict:
        if aDict[x] != bDict[x]:
            deletions += abs(aDict[x] - bDict[x])

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
