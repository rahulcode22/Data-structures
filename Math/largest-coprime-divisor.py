'''
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
'''
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        p=gcd(A,B)
        while p!=1:
            A/=p
            p=gcd(A,B)
        return A
