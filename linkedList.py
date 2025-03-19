class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

current = first
while current:
    print(current.data, end="->")
    current = current.next
print("None")



#create variables first
#  --- similar to seeing the ingredients in a recipe



HW

https://www.geeksforgeeks.org/reverse-a-linked-list/

