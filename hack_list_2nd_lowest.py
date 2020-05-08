
lis=[]
for _ in range(int(input())):
    name = input()
    score = float(input())

    innerlist=[]
    innerlist.append(name)
    innerlist.append(score)
    lis.append(innerlist)

finallist=[]
length=len(lis)
for j in range(length):
    temp = ['', 100.0]
    for i in lis:
        if i[1]<temp[1]:
            temp=i
    finallist.append(temp)
    lis.remove(temp)


l=-1

lmarks=finallist[0][1]
counter=0
sortlist=[]
for i in finallist:

    if i[1]==lmarks:
        if counter==1:
            sortlist.append(i[0])
    else:
        lmarks = i[1]
        counter+=1
        if counter==1:
            sortlist.append(i[0])


xx=sorted(sortlist)
for i in xx:
    print(i)

