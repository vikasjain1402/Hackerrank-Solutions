def checkupper(string):
    for i in string:
        if i.isupper()==True:
            return True
    return False

def checklower(string):
    for i in string:
        if i.islower()==True:
            return True
    return False
def checkisdigit(string):
    for i in string:
        if i.isdigit()==True:
            return True
    return False
def checklsalpha(string):
    for i in string:
        if i.isalpha()==True:
            return True
    return False
def checkisalnum(string):
    for i in string:
        if i.isalnum()==True:
            return True
    return False

if __name__ == '__main__':
    s = input()

    print(checkisalnum(s))
    print(checklsalpha(s))
    print(checkisdigit(s))
    print(checklower(s))
    print(checkupper(s))


#
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.