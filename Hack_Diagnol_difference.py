#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    sumf = 0
    sumr = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i + j == len(arr) - 1:
                sumr = sumr + arr[i][j]
            if i == j:
                sumf = sumf + arr[i][j]
    print(abs(sumr - sumf))


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    diagonalDifference(arr)