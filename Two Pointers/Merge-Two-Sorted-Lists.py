'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input :
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]'''
def merge(arr1,arr2):
    i = 0
    j = 0
    lis = []
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 == 0:
        return arr2
    if n2 == 0:
        return arr1
    while i < n1 and j < n2:
        if arr1[i] > arr2[j]:
            lis.append(arr2[j])
            j += 1
        elif arr1[i] < arr2[j]:
            lis.append(arr1[i])
            i += 1
        else:
            lis.append(arr1[i])
            i += 1
    while i < n1:
        lis.append(arr1[i])
        i += 1
    while j < n2:
        lis.append(arr2[j])
        j += 1
    return lis
arr1 = [1,2]
arr2 = [-1,2]
print merge(arr1,arr2)
