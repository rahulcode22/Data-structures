def rpn(exp):
    stack = []
    for e in exp:
        if e not in ["+", "-", "*", "/"]:
            stack.append(int(e))
        else:
            l, r = stack.pop(), stack.pop()
            if e == "+":
                stack.append(l+r)
            elif e == "-":
                stack.append(l-r)
            elif e == "*":
                stack.append(l*r)
            else:
                if l*r < 0 and l%r != 0:
                    stack.append(l/r + 1)
                else:
                    stack.append(l/r)
    return stack.pop()
