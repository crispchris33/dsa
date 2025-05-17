

class Stack:
    def _init_(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())






class Stack:
def init(self):
self.stack = []

def push(self, value):
self.stack.append(value)

def pop(self):
if not self.is_empty():
return self.stack.pop()
else:
return "Stack is empty!"

def peek(self):
if not self.is_empty():
return self.stack[-1]
else:
return "Stack is empty!"

def is_empty(self):
return len(self.stack) == 0

def size(self):
return len(self.stack)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())

Given an array of integers, find the next greater element for
each element in the array. The next greater element of an
element x is the first greater element on the
right side in the array. If there is no greater
element, return -1 for that position.
input = [4, 5, 2, 10, 8]
output = [5, 10, 10, -1, -1]
def next_greater_element(arr):
stack = []
result = [-1] * len(arr)

for i in range(len(arr) -1, -1, -1):
while stack and stack[-1] <= arr[i]:
stack.pop()

if stack:
result[i] = stack[-1]

stack.append(arr[i])

return result
arr = [4, 5, 2, 10, 8]
arr2 = [4, 5, 0, 10, 12, 1]
result = next_greater_element(arr)
result2 = next_greater_element(arr2)
print("New array", result)
print("New array", result2)