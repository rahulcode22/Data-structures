def reversebit(num):
    n = '{0:032b}'.format(num)
    rev = n[::-1]
    return int(rev,2)

num = 4294967295
print reversebit(num)
