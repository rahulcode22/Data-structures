'''We are given an array of positive integers. Find the pair in array with maximum GCD.'''
def maxGCDPair(arr):
    high = max(arr)
    n = len(arr)
    count = [0]*(high+1)

    for i in range(n):
        count[arr[i]] = 1

    counter = 0
    #Iterating from max to 1
    #GCD is always between MAX and 1
    for i in range(high,0,-1):
        j = i
        #Iterating from curr potential GCD till it is less than max
        while j <= high:
            if count[j] == 1:
                counter += 1
            #Incrementing potential GCD by itself 2i,3i....
            j += i
            if counter == 2:
                return i

arr = [1,2,12,3,6]
print maxGCDPair(arr)
