def mutate_string(string, position, character):
    string1 = ""
    for i in range (len(string)):
        if i == position:
            string1 = string1 + character
        else:
            string1 = string1 + string[i]
    return string1


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)