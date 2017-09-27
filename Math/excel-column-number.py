
# Time:  O(n)
# Space: O(1)

# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
def titleToNumber(num):
    res = 0
    for i in range(len(num)):
        res *=26
        res += ord(num[i])-ord('A')+1
    return result

print titleToNumber("AB")
