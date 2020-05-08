
import itertools as it
x=int(input())
a=[]
for i in input().split(" "):
    a.append(i)
w=int(input())
sum=0
count=0
for i in it.combinations(a,w):
    #print(i)
    count=count+1
    if 'a' in i :

        sum=sum+1
#print(count)
#print(sum)
print('%.4f'%(sum/count))
'''
for i in it.combinations(a,w):
    print(i[0])
'''