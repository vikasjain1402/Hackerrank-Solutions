def print_formatted(number):
   for i in range(1,number+1):
    print(str(i).rjust(len(bin(number))-2," "),end=" ")
    print(oct(i).lstrip("0o").rjust(len(bin(number))-2, " "),end=" ")
    print(hex(i).lstrip("0x").upper().rjust(len(bin(number))-2, " "),end=" ")
    print(bin(i).lstrip("0b").rjust(len(bin(number))-2, " "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)