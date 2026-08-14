#!/bin/python3

"""HackerRank - Plus Minus.

Calcula a proporção de números positivos, negativos e zeros em um array.
"""
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positives = sum(1 for x in arr if x > 0)
    negatives = sum(1 for x in arr if x <0)
    zeros = sum(1 for x in arr if x == 0)
    
    print(f"{positives/n:.6f}")
    print(f"{negatives/n:.6f}")
    print(f"{zeros/n:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
