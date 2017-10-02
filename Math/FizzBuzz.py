'''
Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.
'''
class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, num):

        lis = []
        for i in range(1,num+1):
            if i%3 == 0 and i%5 == 0:
                lis.append("FizzBuzz")
            elif i%3 == 0:
                lis.append("Fizz")
            elif i%5 == 0:
                lis.append("Buzz")
            else:
                lis.append(i)
        return lis
