

def countingValleys(n, s):
    height = 0
    count=0
    for i in s:
        if i == 'U':
            height += 1
        else:
            height -= 1

        if height == 0 and i == 'U':
            print('______')
            count = count + 1

    return count


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)

print(result)