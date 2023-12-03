#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s): 
    res = [j for j in s.split(" ")] 
    res1 = [i.capitalize() for i in res]
    return " ".join(res1)

if __name__ == '__main__':
   s = input()
   #para probar local
   result = solve(s)
   print(result)
    # Para probar en hackerrank
    #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()