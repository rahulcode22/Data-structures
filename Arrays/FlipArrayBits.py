#You are given a binary string(i.e. with characters 0 and 1) S
#consisting of characters S1, S2, …, SN.
#In a single operation, you can choose two indices L and R
#such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR.
#By flipping, we mean change character 0 to 1 and vice-versa.

#Your aim is to perform ATMOST one operation
#such that in final string number of 1s is maximised.
#If you don’t want to perform the operation, return an empty array.
#Else, return an array consisting of two elements denoting L and R.
#If there are multiple solutions,
#return the lexicographically smallest pair of L and R.

def flip(A):
    start =0
    ans = None
    diff = 0
    max_diff = 0

    for i,a in enumerate(A):
        diff +=(1 if a is '0' else -1)

        if diff<0:
            diff = 0
            start = i+1
            continue

        if diff > max_diff:
            max_diff = diff
            ans = [start,i]

    if ans is None:
        return []

    return map(lambda x:x +1,ans)
