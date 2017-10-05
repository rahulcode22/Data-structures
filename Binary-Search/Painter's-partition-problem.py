'''
You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.
'''
def ppp(n,time,arr):
    def isPossible(t,c,a):
        summ = 0
        while a > 0 and len(c) > 0:
            if summ + c[-1] > t:
                summ = 0
                a -=1
            else:
                summ += c.pop()
        if len(c) == 0:
            return True
        else:
            return False

    x = max(arr)
    y = sum(arr)
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return time*arr[0]
    prev = y
    while x < y:
        m = (x + y)/2
        if isPossible(m,arr[:],n):
            prev = m
            y = m - 1
        else:
            x = m + 1
    m = prev
    while isPossible(m-1,arr[:],n):
        m = m - 1
    return m*B % 1000003
