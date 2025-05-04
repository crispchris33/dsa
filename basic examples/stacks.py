#append

stack = []
stack.append(1)
stack.append(2)

#pop - remove from the top

stack = [1, 2]

top_element = stack.pop() # 2

#access top element
stack = [1, 2]

top_element = stack[-1] # 2

#check if stack is empty
stack = [1, 2]

while len(stack) > 0:
    print(stack.pop())



