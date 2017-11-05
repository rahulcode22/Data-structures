'''
We define super digit of an integer x using the following rules:

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of the digit-sum of x. Here, digit-sum of a number is defined as the sum of its digits.

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split())
x = n*k % 9
print x if x else 9
