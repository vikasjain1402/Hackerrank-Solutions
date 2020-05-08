# Enter your code here. Read input from STDIN. Print output to STDOUT
lines=input()
rowschar=input()
line=int(lines)
standpatern='.|.'
patern='---'
for j in range(0,(line)//2):
    print(patern*(((line)//2)-j)+standpatern*((2*j)+1)+patern*(((line)//2)-j))
wellinedash=((line*3)-9)//2
print('-'*(wellinedash)+"-WELCOME-"+'-'*(wellinedash))
for j in range((line)//2,0,-1):
    print(patern*(((line)//2)-(j-1))+standpatern*((2*j)-1)+patern*(((line)//2)-(j-1)))

