'''

N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Example:

Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        c=0
        n=len(A)
        i=0
        state=0
        for i in xrange(len(A)):
            if A[i]==state:
                c+=1
                state=1-state
        return c
            
