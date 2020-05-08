
def climbingLeaderboard(scores, alice):
    res = []
    s = sorted(list(set(scores)))
    for v in alice:
        for i in range(len(s)):
            if  v <s[i] or i==len(s)-1:
                index = i
                if i==len(s)-1 and v>=s[i]:
                    index=i+1
                break
        res.append(len(s) - index +1)
    return res

if __name__ == '__main__':
    fptr = open('rrr.txt', 'w')
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()