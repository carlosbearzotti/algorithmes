#!/bin/python3

"""Teste MBI 2025 - minTime.

Calcula o menor tempo máximo de término agrupando tarefas (arr2) em times de 4
e combinando com os tempos base de arr1.
"""
import math
import os
import random
import re
import sys


#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr1
#  2. INTEGER_ARRAY arr2
#

def minTime(arr1, arr2):
    n = len(arr1)
    arr1.sort()
    arr2.sort(reverse=True)
    
    max_finish_time = 0
    
    for i in range(n):
        group = arr2[i*4:(i+1)*4]
        base = arr1[i]
        finish_time = max(base + x for x in group)
        max_finish_time = max(max_finish_time, finish_time)
        
    return max_finish_time
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr1_count = int(input().strip())

    arr1 = []

    for _ in range(arr1_count):
        arr1_item = int(input().strip())
        arr1.append(arr1_item)

    arr2_count = int(input().strip())

    arr2 = []

    for _ in range(arr2_count):
        arr2_item = int(input().strip())
        arr2.append(arr2_item)

    result = minTime(arr1, arr2)

    fptr.write(str(result) + '\n')

    fptr.close()