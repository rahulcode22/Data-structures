#Given a list of non negative integers,
#arrange them such that they form the largest number.
def largestNumber(self, num):
        # Define customized compare function for sorting
        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return 1
            elif n1+n2 < n2+n1:
                return -1
            else:
                return 0

        num_str = [str(n) for n in num]
        res = ""

        # Sorting according to customized function
        for n in reversed( sorted(num_str,cmp=compare) ):
            res += n

        # Remove unnecessary zeros in head
        res_list = list(res)
        i = 0
        while res_list[i] == '0' and i != len(res)-1:
            i += 1
        res_list = res_list[i:]

        return ''.join( res_list)
