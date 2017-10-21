def xorUptoN(n):
    if n%4 == 0:
        return n
    if n%4 == 1:
        return 1
    if n%4 == 2:
        return n + 1
    else:
        return 0

print xorUptoN(6)
