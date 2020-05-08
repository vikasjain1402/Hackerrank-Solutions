#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair=0
    while len(ar)>=2:
        count=0

        felement=ar[0]
        print(ar[0])
        for i in ar:
            if i==felement:
                count+=1
        pair=pair+count//2
        u=1

        while u<=count:

            ar.remove(felement)
            u=u+1

    return pair

if __name__ == '__main__':

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

