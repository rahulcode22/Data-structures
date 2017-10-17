def findword(matrix,row,col,word):
    x = [-1,-1,-1,0,0,1,1,1]
    y = [-1,0,1,-1,1,-1,0,1]
    #if first vhar of word doesn't match with given starting point in grid
    if matrix[row][col] != word[0]:
        return False
    len_ = len(word)
    #searching words in all directions
    for dir_ in range(8):
        #intialize starting point for curr direction
        rd = row + x[dir_]
        cd = col + y[dir_]
        #first character is already matched,check remaining char
        for k in range(1,len_):
            if rd >= len(matrix) or rd <0 or cd >= len(matrix[0]) or cd < 0:
                break
            #if not matched break
            if matrix[rd][cd] != word[k]:
                break
            rd += x[dir_]
            cd += y[dir_]
        if k == len_:
            return True
    return False

def patternSearch(matrix,word):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if findword(matrix,row,col,word):
                return row,col

matrix = [['G','E','E','K','S','F'],['Q','U','I','Z','Q','A'],['A','B','C','D','E','F']]
print patternSearch(matrix,"GEEKS")
