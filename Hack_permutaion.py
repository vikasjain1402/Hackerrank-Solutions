import itertools

[a,b]=input().split(" ")
a=str(a)[::-1]
c="".join(sorted(a))

for i in itertools.permutations(c,int(b)):
    print("".join(i))
