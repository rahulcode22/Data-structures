'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
'''
def check(s):
    s = s.rstrip(' ')
    s = s.lstrip(' ')
    for i in range(len(s)-1,-1,-1):
        if s[i] == ' ':
            return len(s) - i -1
    return len(s)

s = "  xDGBklKecz IAcOJYOH O  WY WPi"
c = 0
print check(s)
