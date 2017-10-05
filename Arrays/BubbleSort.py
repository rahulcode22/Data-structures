'''
Bubble sort is a example of sorting algorithm . In this method we at first compare the data element in the first position with the second position and arrange them in desired order.Then we compare the data element with with third data element and arrange them in desired order. The same process continuous until the data element at second last and last position
'''
def bubbleSort(arr,n):
    for i in range(0,n):
        for j in range(0,n):
            if arr[j]>arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [3,2,6,4,1]
print bubbleSort(arr,5)
