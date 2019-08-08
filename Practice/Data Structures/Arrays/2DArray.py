#!/bin/python3

# https://www.hackerrank.com/challenges/2d-array/problem

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hgSum = -63
    for x in range (len(arr) - 2):
        for y in range(len(arr) -2):

            num = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1] + arr[x + 2][y] + arr[x + 2][y + 1] + arr[x + 2][y + 2]

            if num > hgSum:
                hgSum = num

    return hgSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
