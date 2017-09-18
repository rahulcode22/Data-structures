#Given an array containing equal number of positive
#and negative elements, arrange the array such that every positive element
#is followed by a negative element.
#Complexity O(n)

t=int(raw_input())
for i in range(t):
    n = int(raw_input())
    arr = map(int,raw_input())
    arr.sort()
    c = 0
    lis = []
    for i in range(len(arr)):
        if arr[i]<0:
            c +=1
        else:
            break

            right = c
            left = c-1
        while left>=0 or right <len(arr):
            lis.append(arr[left])
            lis.append(arr[right])

            right +=1
            left -=1

print lis
