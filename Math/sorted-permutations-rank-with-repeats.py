from itertools import permutations
class Solution:

    def fact (self, n ) :
        if n <= 1 :
            return 1
        else :
            return n * self.fact(n-1)

    def findRank(self, A):

        res = 1
        char_occur = {}
        for char in A:
            char_occur[char] = char_occur.get(char, 0) + 1
        for i in range(0, len(A)-1) :
            rank = 0
            for j in range(i+1, len(A)) :
                if A[i] > A[j] :
                    rank += 1
            temp = self.fact(len(A) - i - 1)%1000003
            temp1= 1
            for key in char_occur.keys() :
                temp1 *= self.fact(char_occur[key])
            temp1 = pow(temp1, 1000001, 1000003)
            res = (res + rank * temp1 * temp)%1000003
            char_occur[A[i]] -= 1
        return res

'''
Another Solution
'''
def fact(n) :
    f = 1
    while n >= 1 :
        f = f * n
        n = n - 1
    return f

# A utility function to count smaller
# characters on right of arr[low]
def findSmallerInRight(st, low, high) :

    countRight = 0
    i = low + 1
    while i <= high :
        if st[i] < st[low] :
            countRight = countRight + 1
        i = i + 1

    return countRight

# A function to find rank of a string
# in all permutations of characters
def findRank (st) :
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0

    while i < ln :

        mul = mul / (ln - i)

        # count number of chars smaller
        # than str[i] fron str[i+1] to
        # str[len-1]
        countRight = findSmallerInRight(st, i, ln-1)

        rank = rank + countRight * mul
        i = i + 1
    for j in set(st):
        if st.count(j) > 1:
            rank = rank/fact(st.count(j))
    return rank + 1


# Driver program to test above function
st = "aba"
print (findRank(st))
