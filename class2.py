O(1): constant time(accessing an array item)

    arr[0]

O(log n): Logarithmic time(Binary search)
O(n): Linear time(Iterating through an array)
O(n^2): Quadratic time(nested loops)




def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        print(f"Processing character: {char}")
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            print(f" Popped element: {top_element}, Stack after popping: {stack}")
        if mapping[char] != top_element:
            print(f" Mismatch found! Expected {mapping[char]}, but got {top_element}")
            return False
        else:
            stack.append(char) #
            print(f" Added to stack: {char}, Stack now: {stack}")

        print(f"Final stack: {stack}")
        return not stack

input1 = "()[]{}"
input2 = "([)]"

print(f"Input: {input1}")
result1 = is_valid(input1)
print(f"Result: {result1}\n")

print(f"Input: {input2}")
result2 = is_valid(input2)
print(f"Result: {result2}")