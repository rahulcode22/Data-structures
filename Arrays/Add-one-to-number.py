#Given a non-negative number represented as an array of digits,

#add 1 to the number ( increment the number represented by the digits ).

#The digits are stored
#such that the most significant digit is at the head of the list.
    def plusOne(self, arr):
        while(arr[0]==0)and len(arr)>1:
            del(arr[0])
        if arr[0]==0 and len(arr)==1:
            arr[0]=1
            return arr
        i=len(arr)-1
        carry=1
        while True:
            value=arr[i]+carry
            if value>=10:
                arr[i]=value%10
                carry=value//10
            else:
                arr[i]=value
                break
            if i==0:
                arr.insert(0,carry)
                break
            i-=1
        return arr
