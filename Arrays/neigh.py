#Solution not completed
from collections import Counter
def neigh(st):
    toCheck = "neigh"
    lis = []
    for i in toCheck:
        lis.append(st.count(i))
    min_ =min(lis)
    if len(set(lis)) == 1:
        return min_
    else:
        return min_

st = 'n'
print neigh(st)
