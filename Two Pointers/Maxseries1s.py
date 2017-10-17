class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, arr, m):
        wl ,wr =0, 0
        bestl, bestWin = 0, 0
        zeroCount = 0
        n = len(arr)
        lis = []
        while wr < n:
            if zeroCount <= m:
                if arr[wr] == 0:
                    zeroCount += 1
                wr += 1
            if zeroCount > m:
                if arr[wl] == 0:
                    zeroCount -= 1
                wl += 1
            if (wr - wl > bestWin):
                bestWin = wr - wl
                bestl = wl
        for i in range(bestWin):
            lis.append(bestl+i)
        return lis
