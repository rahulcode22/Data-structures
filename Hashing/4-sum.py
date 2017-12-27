'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, arr, target):
        i = 0
        j = 1
        flag = 0
        n = len(arr)
        ans = []
        if n < 4:
            return ans
        arr.sort()
        while i < n-3:
            j = i+1
            while j < n-2:
                num = target - (arr[i]+arr[j])
                k = j+1
                l = n-1
                while k < l:
                    sum_ = arr[k]+arr[l]
                    if sum_ == num:
                        ans.append([arr[i],arr[j],arr[k],arr[l]])
                        while arr[k] == arr[k+1] and k < n-2:
                            k += 1
                        while arr[l] == arr[l-1] and l > 0:
                            l -= 1
                        k += 1
                        l -= 1
                    elif sum_ < num:
                        k += 1
                    else:
                        l -= 1
                while arr[j] == arr[j+1] and j < n-2:
                    j += 1
                j += 1
            while arr[i] == arr[i+1] and i < n-2:
                i += 1
            i += 1
        return ans
