import itertools

[a,b]=input().split(" ")
a=str(a)[::-1]
c="".join(sorted(a))
for j in range(1,int(b)+1):
    for i in itertools.combinations(c,j):
        print("".join(i))