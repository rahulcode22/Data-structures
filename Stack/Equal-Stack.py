'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.
'''
n1, n2, n3 = map(int,raw_input().split(' '))
h1 = map(int,raw_input().split())[::-1]
h2 = map(int,raw_input().split())[::-1]
h3 = map(int,raw_input().split())[::-1]

sum_h1 = sum(h1)
sum_h2 = sum(h2)
sum_h3 = sum(h3)

while not ((sum_h3 == sum_h2) and (sum_h1 == sum_h2)):

    if sum_h1 > sum_h2 and sum_h1 > sum_h3:
        t = h1.pop()
        sum_h1 -= t

    if sum_h1 < sum_h2 and sum_h2 > sum_h3:
        t = h2.pop()
        sum_h2 -= t

    if sum_h1 < sum_h3 and sum_h2 < sum_h3:
        t = h3.pop()
        sum_h3 -= t

print sum_h1
