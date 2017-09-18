#Given an array.
#The task is to choose K numbers from the array
#such that the absolute difference between the sum of chosen numbers
#and the sum of remaining numbers is maximum.

sum1=sum2=0
arr = [8,4,5,2,10]
k = 2
n=len(arr)
arr=sorted(arr)

if k<n-k:
    sum1 =sum(arr[0:k])
    sum2 = sum(arr[k:])
else:
    sum1 = sum(arr[k:])
    sum2 = sum(arr[0:k])
print  abs(sum1-sum2)
