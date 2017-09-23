"""You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array,
then the whole array should get sorted.
If A is already sorted, output -1."""
def unsorted(arr):
    l = 0
    r = len(arr)-1
    s = sorted(arr)
    i = 0
    n=  len(arr)
    while l<n and arr[l] == s[l]:
        l +=1
    while r >0 and arr[r] == s[r]:
        r -=1

    if arr == s:
        return [-1]
    else:
        return [l,r]

arr = [1,3,2,4,5]
print unsorted(arr)
