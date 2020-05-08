
def printpattern(n):
    n+=1
    list = []
    for i in range(0, 26):
        list.append("%c" % (97 + i))
    for i in range(n-1,-1,-1):
        if i==(n-1) :
            if n==1:
                print(list[i] , end="")
            else:
                print((list[i]+"-"),end="")
        else:
            print((list[i]+"-"),end="")

    for j in range(1,n):
        if j == (n-1):
            print(list[j] , end="")
        else:
            print((list[j] + "-"), end="")
n=5
for i in range(n):
    print("-"*((2*n)-(2*(i+1))),end="")
    printpattern(i)
    print("-"*(2*n-2*(i+1)))
for i in range(n-1,0,-1):
    print("-"*((2*n)-(2*(i))),end="")
    printpattern(i-1)
    print("-"*(2*n-2*(i)))








