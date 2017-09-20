"""Given an unsorted array, f
ind the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space."""

def maximumGap(arr):

    arr.sort()
    n = len(arr)
    if n<= 2:
        return 0
    maximum = 0
    start_index = 0
    for i in range(1,n):
        if arr[i]-arr[start_index] > maximum:
            maximum = arr[i] - arr[start_index]
            start_index += 1
        else:
            start_index += 1
    return maximum

arr = [1, 10, 5]
print maximumGap(arr)
