#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pangrams function below.
def pangrams(s):
    smallalpha = "abcdefghijklmnopqrstuvwxyz"

    s_low = s.lower()
    for word in s_low:
        for refs in smallalpha:
            if word == refs:
                smallalpha = smallalpha.replace(word, "")

    ans = "not pangram"
    if len(smallalpha) == 0:
        ans = "pangram"

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
