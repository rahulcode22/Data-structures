class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):

        if -10 < A < 10:
            return A

        ans = int(str(A).lstrip('-')[::-1])
        ans = -1 * ans if A < 0 else ans

        if not (-2147483648 < ans < 2147483647):
            return 0
        else:
            return ans 
