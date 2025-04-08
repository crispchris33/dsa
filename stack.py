class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return
        else:
            return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return
        
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    


s = Stack()
s.push(4)
print(s.pop())
print(s.peek())
s.push(5)
s.push(6)
print(s.peek())    