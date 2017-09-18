Given an array of n integers and a number, k, perform k left rotations on the array. Then print the updated array as a single line of space-separated integer
def array_left_rotation(a, n, k):
    arr=[0]*n
    for i in range(n):

        arr[i%n] = a[(i+k)%n]
    return arr


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
