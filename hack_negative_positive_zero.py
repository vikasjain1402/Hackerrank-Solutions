#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    cpositive=0
    czero=0
    cnegative=0
    for i in range(len(arr)):
        if arr[i] >0:
            cpositive+=1
        elif arr[i]<0:
            cnegative+=1
        else:
            czero+=1

    print('%.6f'%(cpositive/len(arr)))
    print('%.6f'%(cnegative/len(arr)))
    print('%.6f'%(czero/len(arr)))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
