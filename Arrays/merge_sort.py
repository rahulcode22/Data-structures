def merge(arr, s1, s2):

    i=j=0
    while i+j < len(arr):
        if j == len(s2) or (i<len(s1) and s1[i]<s2[j]):
            arr[i+j] = s1[i] #Copy ith element of S1 as next item of arr
            i =i+1
        else:
            arr[i+j] = s2[j] #Copy jth element of S2 as next item of arr
            j = j+1

def mergeSort(arr):
    n = len(arr)
    if n<2:
        return
    #divide
    mid = n//2
    s1 = arr[0:mid]
    s2 = arr[mid:n]

    #Conquer (with recursion)
    mergeSort(s1)
    mergeSort(s2)

    #merge results
    merge(arr,s1,s2)
    return arr

arr = [1,2,5,3,9,6]
print "array before sorting"
print arr
print "array after sorting"
print mergeSort(arr)
