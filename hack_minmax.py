

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print(sum(arr)-max(arr),end=" ")
    print(sum(arr)-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
