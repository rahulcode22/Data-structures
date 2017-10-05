from math import floor
def sqrtsearch(x):
    start = 1
    end  = x
    ans = 0
    if x == 0 or x == 1:
        return x
    while start <= end:
        mid = (start+end)/2
        if x == mid*mid:
            return mid
        elif x > (mid*mid):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return floor(ans)

x = 11
print sqrtsearch(x)
