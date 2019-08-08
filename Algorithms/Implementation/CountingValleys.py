#!/bin/python3

# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
