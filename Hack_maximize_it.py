# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as iter

(K,M)=input().split(" ")
list=[]

for j in range(int(K)):
    innerlist = []
    for i in input().split(" ")[1:]:
        innerlist.append(int(i))
    list.append(innerlist)

#print(list)
value=0
for i in iter.product(*list):
    sm = 0
    for j in i:
        sm=(sm+(j**2))
    if (sm%int(M))>value%(int(M)):
        value=sm
print(value%int(M))



