#Find out the maximum sub-array of non negative numbers from an array.
#The sub-array should be continuous.
#That is, a sub-array created by choosing the second and fourth element
#and skipping the third element is invalid.

#Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
#Sub-array A is greater than sub-array B if sum(A) > sum(B).


def LongestSum(arr):
    currSum = currStart = currLength = maxSum = maxStart = maxLength = 0
    for i in range(len(arr)):
        if arr[i]<0:
            if (currSum>maxSum) or (currSum == maxSum and currLength>maxLength):
                maxSum = currSum
                maxLength = currLength
                maxStart = currStart
            currStart = i+1
            currSum = currLength =0
        else:
            currSum += arr[i]
            currLength +=1

    if (currSum>maxSum) or (currSum == maxSum and currLength>maxLength):
        maxSum = currSum
        maxLength = currLength
        maxStart = currStart
    return arr[maxStart:maxStart+maxLength]
#Main Driver Program
arr=[1,2,5,-7,2,3]
print LongestSum(arr)
