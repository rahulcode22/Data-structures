def sort012(arr):
    n = len(arr)
    hi = n - 1
    low = 0
    high = n - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [0,1,1,0,1,1,0,0,0,1]
print sort012(arr)
