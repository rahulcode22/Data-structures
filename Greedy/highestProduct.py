arr = map(int,raw_input().split())
max_ = float('inf')
n = len(arr)
arr = sorted(arr, reverse = True)
max_ = arr[0]*arr[1]*arr[2]
to_check = arr[n-1]*arr[n-2]
if max_ > arr[0]*to_check:
    print max_
else:
    print arr[0]*to_check
