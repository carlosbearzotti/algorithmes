#!/bin/python3

"""Teste MBI 2025 - getDistinctOneCounts.

Conta quantos valores distintos de número de 1s podem ser obtidos invertendo
zeros para 1s em um segmento do array binário.
"""
import math
import os
import random
import re
import sys


#
# Complete the 'getDistinctOneCounts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getDistinctOneCounts(arr):
    n = len(arr)
    original_ones = sum(arr)
    distinct_counts = set()
        
    for i in range(n):
        ones = 0
        zeros = 0
        for x in range(i, n):
            if arr[x] == 1:
                ones += 1
            else: 
                zeros += 1
            delta = zeros - ones
            new_count = original_ones + delta
            distinct_counts.add(new_count)
    
    distinct_counts.add(original_ones)
    
    return len(distinct_counts)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getDistinctOneCounts(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
