def integerToRoman(num):
    m = ["", "M" ,"MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L" ,"LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    thousands = m[num/1000]
    hundreds = c[(num%1000)/100]
    tens = x[(num%100)/10]
    ones = i[num%10]
    ans = thousands + hundreds + tens + ones
    return ans

print integerToRoman(3549)
