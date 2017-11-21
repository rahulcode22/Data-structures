def wordBreak(s,dic):
    segmented = [True]
    for i in range(len(s)):
        segmented.append(False)
        for j in range(i,-1,-1):
            if segmented[j] and s[j:i+1] in dic:
                segmented[i+1] = True
                break
    return segmented[len(s)]
s = "myinterviewtrainer"
dic = ["interview","my","trainer"]
print wordBreak(s,dic)
