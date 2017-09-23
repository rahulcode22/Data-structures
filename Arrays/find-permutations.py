"""Given a positive integer n and a string s consisting only of letters D or I,
you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater."""
def findPerm(arr, b):
    ans = range(1,b+1)
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == "D":
            cnt +=1
        else:
            ans[i-cnt:i+1] = ans[i-cnt:i+1][::-1]
            cnt =0
    if arr[-1] == "D":

        ans[len(arr) - cnt:len(arr) +1] = ans[len(arr) - cnt:len(arr)+1][::-1]
    return ans
