def lengthOfLongestSubstring(arr):
    max_length = 0
    i = 0
    j = i+1
    n = len(arr)
    ans = arr[0]
    while j < n:
        if arr[j] not in arr[i:j]:
            len_ = len(arr[i:j+1])
            if len_ > max_length:
                max_length = len_
                ans = arr[i:j+1]
            j += 1
        else:
            i += 1
            j = i+1
    return ans


s = raw_input()
print lengthOfLongestSubstring(s)


#Approach 2
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        prev = {c:-1 for c in A}
        best, prev_best = 1, 1
        for i in range(1, len(A)):
            prev[A[i-1]] = i-1
            prev_best = min(i-prev[A[i]], prev_best+1)
            best = max(best, prev_best)
        return best
