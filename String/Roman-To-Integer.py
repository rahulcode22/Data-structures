'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
def value(num):
    if num == 'X':
        return 10
    if num == 'I':
        return 1
    if num == 'V':
        return 5
    if num == 'L':
        return 50
    if num == 'C':
        return 100
    if num == 'D':
        return 500
    if num == 'M':
        return 1000

def romanToInteger(roman):
    res = 0
    i = 0
    while i < len(roman):
        value1 = value(roman[i])
        if i+1 < len(roman):
            value2 = value(roman[i+1])
            if value1 >= value2:
                res += value1
                i += 1
            else:
                res += value2 - value1
                i += 2
        else:
            res = res + value1
            i += 1
    return res
roman = "XXXIV"
print romanToInteger(roman)
