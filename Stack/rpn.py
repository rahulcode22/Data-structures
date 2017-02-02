def rpn(s):
    var_list=[]
    sym_list=[]
    for c in s:
        if c >='a' and c <='z':
            var_list.append(c)
        elif c in ['^', '*', '/', '+', '-']:
            sym_list.append(c)
        elif c == ')':
            x=var_list.pop()
            y=var_list.pop()
            z=sym_list.pop()
            var_list,append(x+y+z)
    return var_list[0]
s=raw_input()
print rpn(s)
            
