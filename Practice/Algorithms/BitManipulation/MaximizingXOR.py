#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximizingXor function below.
def maximizingXor(l, r):
    maxval = 0

    for f in range(l, r + 1, 1):
        for s in range(l, r + 1, 1):
            if (f ^ s) > maxval:
                maxval = f ^ s

    return maxval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
