'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.

'''
def countAndSay(n):
    s = '1'
    for i in range(n-1):

        let ,temp ,count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count) + let
                let = l
                count = 1
        temp += str(count) + let
        s = temp
    return s

print countAndSay(4)
