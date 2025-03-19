# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# first = Node(10)
# second = Node(20)
# third = Node(30)

# first.next = second
# second.next = third

# current = first
# while current:
#     print(current.data, end="->")
#     current = current.next
# print("None")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next   
        last.next = new_node
        
    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
    def delete_head(self):
        if self.head is None:
            print("No nodes!")
            return
        self.head = self.head.next

    def delete_node(self, data):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def reverse_list(self):
        prev, curr = None, self.head
            
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev





llist = LinkedList()
llist.insert_at_end(10)        
llist.insert_at_end(20)        
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_beg(5)
llist.delete_node(30)


# print("Linked List: ", llist.display())
# llist.delete_head()


# print("Linked List: ", llist.display())

print("Original List:")
llist.display()

llist.reverse_list()

print("Reversed List:")
llist.display()




# 10->20->30->40
# case 1: delete the head
    # Access, Assign, Delete
# case 2: delete not the head
    # keep track of the previous one (delete data)
    
# Reverse the LinkedList