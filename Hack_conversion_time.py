#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    x = s.split(":")
    ampm = x[2][2:4]

    if ampm == 'AM':
        hr = x[0]
        if hr == '12':
            hr = "00"

        min = x[1]
        sec = x[2][0:2]
        return hr + ":" + min + ":" + sec
    else:
        hr = x[0]
        if hr == '12':
            pass
        else:
            hr = str(int(x[0]) + 12)
        min = x[1]
        sec = x[2][0:2]
        return hr + ":" + min + ":" + sec


if __name__ == '__main__':

    s = input()
    print(timeConversion(s))

