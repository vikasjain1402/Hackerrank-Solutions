# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
► It must start with a 4,5or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digit
'''
def startwith(string):
    return [False,True][string[0]=='4' or string[0]=='5' or string[0]=='6']

def check_count(string):
    count=0
    for i in string:
        if i.isdigit()==True:
            count=count+1
    return [False ,True] [count==16]

def check_digits(string):
    for i in string :
        return [False,True][i.isdigit()==True or i=='-']

def check_group4(string):
    if string.count("") > 17:
        for i in range(4):
            if len(string.split('-')[i])!=4:
                return False
            else :
                pass
    return True

def check_repeat(string):
    li=[]
    for i in string:
        if i.isdigit()==True:
            li.append(i)
    for i in range(len(li)-3):
        if li[i]==li[i+1]==li[i+2]==li[i+3]:
            return False

    return True





number=int(input())
list=[]

for i in range(number):
    list.append(input())

for i in list:
    x=startwith(i) and \
    check_count(i) and\
    check_digits(i) and \
    check_group4(i) and \
    check_repeat(i)
    if x== True :
        print('Valid')
    else:
        print('Invalid')