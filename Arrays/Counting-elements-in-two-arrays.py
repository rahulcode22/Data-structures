#Given two unsorted arrays arr1[] and arr2[].
#They may contain duplicates.
#For each element in arr1[] count elements
#less than or equal to it in array arr2[].
#complexity O(n)
def binary_search(arr,n,x):
    l=0
    h=n-1
    while(l<=h):
        mid = (l+h)/2
        if arr[mid]>x:
            h=mid-1
        else:
            l=mid+1
    #required index
    return h
def countElements(arr1,arr2,m,n):
    arr2.sort()
    for i in range(m):
        #Last index of largest element smaller than or equal to x
        index = binary_search(arr2,n,arr1[i])

        print index+1

arr1 = [1,2,3,4,7,9]
arr2 = [0,1,2,1,1,4]
m=len(arr1)
n=len(arr2)
countElements(arr1, arr2, m, n)
