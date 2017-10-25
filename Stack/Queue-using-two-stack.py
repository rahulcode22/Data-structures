class QueueTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self,item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:

            while self.in_stack:
                new_item = self.in_stack.pop()
                self.out_stack.append(new_item)

                if len(self.out_stack) == 0:
                    raise IndexError("Can't dequeue an empty stack")
        return self.out_stack.pop()

s = QueueTwoStacks()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
print s.dequeue()
