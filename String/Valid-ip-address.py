'''Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)'''
def validIpAddress(st):
    temp = []
    def is_valid(x):
        return x and int(x) < 256 and not (s.startwith('0') and len(x) > 1)
    for i in range(1,4):
        if not is_valid(st[:i]):
            continue
        for j in range(i,i+4):
            if not is_valid(st[i:j]):
                continue
            for l in range(j,j+4):
                if not (is_valid(st[j:l]) and is_valid(st[l:])):
                    continue
                ip = st[:i], st[i:j], st[j:l], st[l:]
                temp.append('.'.join(ip))
    return sorted(temp)
