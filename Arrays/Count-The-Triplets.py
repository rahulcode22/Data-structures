#Given an array of distinct integers.
#The task is to count all the triplets
#such that sum of two elements equals the third element.
#Complexity O(n^2)
def findTriplet(arr):
    arr.sort()
    n = len(arr)
    i = n-1
    count = 0
    while(i>=0):
        j=0
        k=i-1
        if (arr[i]==arr[j]+arr[k]):
            count +=1
        elif (arr[i]>arr[j]+arr[k]):
            j +=1
        else:
            k -=1
        i=i-1

    return count

arr = [5,32,1,7,10,50,19,21,2]
print findTriplet(arr)
