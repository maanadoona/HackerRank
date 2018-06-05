#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    dic_arr = {}
    dic_brr = {}
    list_comp = []
    for a in arr:
        if a in dic_arr.keys():
            dic_arr[a] += 1
        else:
            dic_arr[a] = 1
    for a in brr:
        if a in dic_brr.keys():
            dic_brr[a] += 1
        else:
            dic_brr[a] = 1

    for k, v in dic_arr.items():
        if k in dic_brr.keys():
            if v != dic_brr[k]:
                list_comp.append(k)

    return list_comp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
