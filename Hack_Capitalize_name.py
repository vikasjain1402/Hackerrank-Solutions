import string
def solve(s):
    x=s.split(" ")
    v=[]
    for i in x:
        v.append(i.capitalize())
    return(" ".join(v))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    print(result)
    #fptr.write(result + '\n')
    #fptr.close()
