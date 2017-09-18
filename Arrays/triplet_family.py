
arr = [5,32,1,7,10,50,19,21,0]
var = False
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if (arr[i]+arr[j]) in arr:
            var=  True

if var:
    print "1"
else:
    print "-1"
