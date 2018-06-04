#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumLoss function below.
def minimumLoss(price):
    years = len(price)
    diff = []
    for i in range(0, years - 1, 1):
        for j in range(i + 1, years, 1):
            if price[i] >= price[j]:
                diff.append(price[i] - price[j])

    ans = min(diff)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
