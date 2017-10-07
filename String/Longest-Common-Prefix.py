'''
Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.
'''
def checkPrefix(prefix,st):
    j = 0
    len_ = 0
    for i in range(len(prefix)):
        if st[i] != prefix[j]:
            break
        j += 1
        len_ +=1
    return prefix[0:len_]

def LCP(arr):
    min_ = len(arr[0])
    index = 0
    for i in range(1,len(arr)):
        m = len(arr[i])
        if m < min_:
            min_ = m
            index = i
    prefix = arr[index]
    for i in arr:
        prefix = checkPrefix(prefix,i)

    return prefix

arr = [ "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" ]
print LCP(arr)






#Divide and Conquer Approach
def commonPrefix(st1,st2):
    j = 0
    len = 0
    for i in range(min(len(st1),lem(st2))):
        if st1[i] != st2[j]:
            break
        else:
            j += 1
            len += 1
    return st1[0:len]


def LongestCommonPrefix(arr):
    low = 0
    high = len(arr)
    if low == high:
        return arr[low]
    if  low < high:
        mid = (high - low)/2
        st1 = LongestCommonPrefix(arr,low,mid)
        st2 = LongestCommonPrefix(arr,mid+1,high)

        return commonPrefix(st1,st2)
