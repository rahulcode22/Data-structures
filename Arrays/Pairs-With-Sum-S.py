s=10
arr = [1,3,7,4,6,9]
for i in range(len(arr)):
    if (s-arr[i]) in arr:
        print arr[i],arr[arr.index(s-arr[i])]
