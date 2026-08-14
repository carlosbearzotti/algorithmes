#!/bin/python3

"""Teste MBI 2025 - changeAds.

Inverte os bits da representação binária de um inteiro e retorna o novo valor.
"""
import math
import os
import random
import re
import sys


#
# Complete the 'changeAds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER base10 as parameter.
#

def changeAds(base10):
    
    bin_str = bin(base10)[2:]
    
    flipped = ''.join('1' if c == '0' else '0' for c in bin_str)
    
    return int(flipped, 2)

if __name__ == '__main__':