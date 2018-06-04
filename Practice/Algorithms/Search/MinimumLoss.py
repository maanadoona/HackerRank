#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumLoss function below.
def minimumLoss(p):
    sprice = sorted(price, reverse=True)
    diffList = []

    for i in range(len(sprice) - 1):
        diffList.append(sprice[i] - sprice[i + 1])
    print(diffList)

    sdiffList = sorted(diffList)
    print(sdiffList)

    if min(sdiffList) == max(sdiffList):
        ans = min(sdiffList)
    else:
        for item in sdiffList:
            pos1 = diffList.index(item)
            print(pos1)
            print(price.index(sprice[pos1]), price.index(sprice[pos1 + 1]))
            if price.index(sprice[pos1]) < price.index(sprice[pos1 + 1]):
                ans = item
                break

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
