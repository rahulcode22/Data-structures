#Given numRows, generate the first numRows of Pascal’s triangle.

#Pascal’s triangle :
#To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

def generate(n):
    arr = [[0 for _ in range(n) ] for _ in range(n)]
    for line in range(0,n):
        for i in range(0,line+1):
            if line == i or i == 0:
                arr[line][i] = 1
            else:
                arr[line][i] = arr[line-1][i-1]+arr[line-1][i]

    for i in arr:
        for j in arr:
            if 0 in j:
                j.remove(0)
    return arr

n=5
print generate(n)
