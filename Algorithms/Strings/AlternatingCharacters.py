#!/bin/python3

# https://www.hackerrank.com/challenges/alternating-characters/problem

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0

    for ind, ch in enumerate(s[:-1]):
        if ch == s[ind + 1]:
            deletions += 1

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
