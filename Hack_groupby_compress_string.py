from itertools import groupby
a=[]
b=[]
things=input()
for key, group in groupby(things):
    a.append(key)
    b.append(list(group))
t=()
for i in b:
    t=len(i),int(i[0])
    print(t,end=" ")