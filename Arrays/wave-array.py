#Given an array of integers,
#sort the array into a wave like array and return it,
#In other words, arrange the elements into a sequence
#such that a1 >= a2 <= a3 >= a4 <= a5.....
def solve(arr):
    arr.sort()
    n = len(arr)
    array =[0]*len(arr)
    for i in range(0,n,2):

        if i  ==n-1:
            array[i] = arr[i]
        else:
            array[i+1] = arr[i]

    for j in range(1,n,2):
        array[j-1] = arr[j]

    return array

arr = [5,1,3,2,4]
print solve(arr)
