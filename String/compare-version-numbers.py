'''
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1, v2 = (map(int, v.split('.')) for v in (version1, version2))
        d = len(v2) - len(v1)
        return cmp(v1 + [0]*d, v2 + [0]*-d)


'''
Without inbuilt function Approach
'''
def compare(v1,v2):
    v1 = v1.split('.')
    v2 = v2.split('.')
    while v1 !=[] and int(v1[-1] == 0):
        v1.pop()
    while v2 != []  and int(v2[-1] == 0):
        v2.pop()
    m = min(len(v1,v2))
    for i in range(m):
        a = v1[i]
        b = v2[i]
        if a > b:
            return 1
        elif a < b:
            return -1
    if len(v1) > len(v2):
        return 1
    if len(v1) == len(v2):
        return 0
    return -1
