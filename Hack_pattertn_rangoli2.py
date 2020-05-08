def printpattern(n, max):
    n += 1
    list = []
    for i in range(0, 26):
        list.append("%c" % (97 + i))
    for i in range(0, n):
        if i == (0):
            if n == 1:
                print(list[max - 1 - i], end="")
            else:
                print((list[max - 1 - i] + "-"), end="")
        else:
            print((list[max - 1 - i] + "-"), end="")
    for j in range(n - 1, 0, -1):
        if j == (1):
            print(list[max - j], end="")
        else:
            print((list[max - j] + "-"), end="")


def print_rangoli(n):
    for i in range(n):
        print("-" * ((2 * n) - (2 * (i + 1))), end="")
        printpattern(i, n)
        print("-" * (2 * n - 2 * (i + 1)))
    for i in range(n - 1, 0, -1):
        print("-" * ((2 * n) - (2 * (i))), end="")
        printpattern(i - 1, n)
        print("-" * (2 * n - 2 * (i)))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

