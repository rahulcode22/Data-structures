#uses python2
def merge(a,b):
    if a is None:
        return b
    if b is None:
        return a
    if (a.data <=b.data):
        res=a
        res.next=merge(a.next,b)
    else:
        res=b
        res.next=merge(a,b.next)
    return res
