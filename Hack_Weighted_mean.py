# Enter your code here. Read input from STDIN. Print output to STDOUT

x=int(input())
a=[]
w=[]
sum=0
weight=0

for i in input().split(" "):
    a.append(int(i))

for i in input().split(" "):
    w.append(int(i))

for i in range(x):
    sum=sum+(a[i]*w[i])

for i in w:
    weight=weight+i

print("%.1f"%(sum/weight))