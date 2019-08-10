#!/bin/python3

# https://www.hackerrank.com/challenges/arrays-ds/problem

import os

# Complete the reverseArray function below.
def reverseArray(a):

    counter = 0
    newArr = [None] * len(a)

    for x in reversed(a):
        newArr[counter] = x
        counter += 1

    return newArr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
