class twostack:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        top2=size
    #pushing item x in stack1
    def push1(x):
        if top1 < top2-1:
            top1 = top1+1
            arr[top1] = x
        else:
            print "stack overflow"
            exit(1)
    #method to push an element x to stack2
    def push2(x):
        if top1 < top2-1:
            top2 -= 1
            arr[top2] = x
        else:
            print "Stack Overflow"
            exit(1)
    #method to pop an element from first stack
    def pop1(self):
        if top1 >= 0:
            x = self.arr[self.top1]
            top1 = top1-1
            return x
        else:
            print "stack underflow"
            exit(1)
    def pop2(self):
        if top2 <= slf.size:
            x = self.array[self.top2]
            self.top2 = self.top2+1
            return x
        else:
            print "stack underflow"
            exit()
