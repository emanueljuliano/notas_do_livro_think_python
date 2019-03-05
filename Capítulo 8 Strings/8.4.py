def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
#return True if the first letter is lower and False if it's higher

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
#always return 'True'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
#return True if the last letter is lower,  False if it is another thing and if the string has len == 0, an error occurs

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
#return True if the last letter is lower and False if there's nothing or it's something else

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True
#return False if there is any letter who isn't lower and True if all the letters are lower
