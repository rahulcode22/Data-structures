#Give an unsorted integer array, find the first missing positive integer
def firstMissingPositive(arr):
    length = len(arr)
    maximum = max(arr)

    if maximum < 0 :
        return 1
    value = [None]*max(maximum,length)

    for i in arr:
        if i > 0:
            value[i-1] = 1

    for i,data in enumerate(value):
        if data == None:
            return i+1

    return i+2

arr = [1,2,0]
print firstMissingPositive(arr)
