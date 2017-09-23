#Hacker block Daily Code Byte
"""Sanjay has a new job for which he needs your help!
He gets a list of employees with their salary.
The maximum salary is 100.

Sanjay is supposed to arrange the list in such a manner that the list is sorted in decreasing order of salary.
And if two employees have the same salary, they should be arranged in
lexicographical manner such that the list contains only names of those employees having salary greater than or equal to a given number x.

Help Sanjay prepare the same!"""
import operator
x = 79
n = 4
lis = {'Eve':78 ,'Bob':99,'Suzy':86,'Alice':86}
sorted_dic = sorted(lis.items(), key =operator.itemgetter(1))
for i in sorted_dic[::-1]:
    if i[1]>=x:

        print i[0] , i[1]
