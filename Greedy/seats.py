arr = map(str,raw_input().split())
n = len(arr)
index_lis = [i for i in range(n) if arr[i] == 'x']
index_len = len(index_lis)
if index_len <=1 :
    print 0
median = 0
if index_len%2 == 1:
    median = index_lis[index_len/2]
else:
    median = (index_lis[index_len/2] + index_lis[index_len/2 - 1] + 1)/2
step = 0
target = median
for i in range((index_len-2)/2,-1,-1):
    step += target-index_lis[i]
    target -= 1
target = median
for i in range(index_len/2,index_len):
    step += index_lis[i] - target
    target += 1
print step%10000003
