# ==============================
# Doubly Linked List Methods
# ==============================

# Insert Methods
# --------------------------------
# insert_head(value)      → Inserts a node at the beginning (head).
# insert_tail(value)      → Inserts a node at the end (tail).
# insert_at(index, value) → Inserts a node at a specific index.

# Delete Methods
# --------------------------------
# delete_at(index)        → Deletes a node at a specific index.
# delete_node_by_value(value) → Deletes the first node that matches the given value.
# delete_nth_node_end(value) → Deletes the nth node from the end.

# Search & Get Methods
# --------------------------------
# search(value)          → Searches for a value and returns True if found, else False.
# get_at(index)          → Returns the data at a given index.

# Print Methods
# --------------------------------
# print_list()           → Prints the list from head to tail.
# print_reverse()        → Prints the list from tail to head (does not modify it).

# Size & Reverse Methods
# --------------------------------
# size()                 → Returns the number of nodes in the list.
# reverse()              → Reverses the list in-place by swapping next and prev pointers.
# dummy_reverse()        → Creates a new reversed list (without modifying the original).

# Sorting & Duplicate Removal
# --------------------------------
# sort_and_remove_dups() → Sorts the list and removes duplicate values.


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value) #create new node
        new_node.next = self.head #move header +1

        if self.head: 
            self.head.prev = new_node #after moving prev header forware 1, assign previous header node back link to new head node
        else:
            self.tail = new_node #if the list was empty, it has to be a head and tail

        new_node.prev = None #since we made a head node, it doesnt have a previous
        self.head = new_node #assigning the head of the linked list


    def insert_tail(self, value):
        new_node = Node(value)  #create the node
        new_node.prev = self.tail #assigning the back link of the new node

        if self.tail:           #if the list exists
            self.tail.next = new_node #assigning the forward link to the previous last node
        else:                   #if the list was empty
            self.head = new_node  #if it was empty before, we have to make the header info also

        self.tail = new_node  #assigning the tail node
        new_node.next = None  #the new tail node doesnt have a forward pointer

    def insert_at(self, index, value):
        if index == 0:   #insert at head----
            self.insert_head(value)
            print(f'No list existed, value inserted at head')
            return
        
        new_node = Node(value)  #creating the node
        curr = self.head        
        count = 0

        while curr is not None and count < index - 1: #traversing to 1 before insertion point
            curr = curr.next
            count += 1

        if curr is None:  #if the requested index does not exist
            print(f"Insert at failed, invalid index")
            return
        
        new_node.next = curr.next  #connecting the new node forward pointer

        if curr.next:  #if there was a node infront, 
            curr.next.prev = new_node  #connect the back link to the new node
        
        curr.next = new_node  #updating the forward link
        new_node.prev = curr   #connecting the new node back to curr

        if new_node.next is None:   #if we are inserting at the last point,
            self.tail = new_node    #assigning linked list tail

    def delete_at(self, index):
        if self.head is None:
            print(f"Delete at failed, invalid index")
            return
        
        if index == 0:   #if we need to delete the head node 'index 0'
            self.head = self.head.next 
            if self.head:
                self.head.prev = None
            else:
                self.tail = None   #if the list becomes empty, update the tail
            return
        
        curr = self.head
        count = 0

        while curr is not None and count < index:
            curr = curr.next
            count += 1

        if curr is None:
            print(f"Delete at failed, invalid index")
            return
        
        if curr.next: #link the next node's prev to the prev node
            curr.next.prev = curr.prev  #linking forward node to the prev link

        if curr.prev:
            curr.prev.next = curr.next #linking prev node to the next node

        if curr.next is None:  #deleting the tail
            self.tail = curr.prev

    def search(self, value):  #same for the single linked list actually
        curr = self.head

        while curr:
            if curr.data == value:
                return True
            else:
                curr = curr.next

        return False

    def get_at(self, index): #essentially the same as the single LL also
        curr = self.head
        count = 0

        while curr and count < index:
            curr = curr.next
            count += 1

        if curr is None:
            return None
        
        return curr.data

    def print_list(self):
        if self.head is None:
            return print("Empty List") 
    
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next #move to next node
        
    def size(self):  #again, same as in the single linked list
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.next
        return count
    
    def reverse(self):  #reversing with reassignments(in place reversal)
        if self.head is None:     #empty case
            return print(f"List does not exist")

        if self.head == self.tail:  #1 node case
            return print(f'Cannot reverse, only one node: {self.head.data}')

        curr = self.head #start at head of current list

        while curr:   #keep going until the end
            temp = curr.next    #save the next node before changing it
            curr.next = curr.prev  #flip the next pointer to point backwards
            curr.prev = temp        #flip the previous pointer to point forward
            curr = temp     #move to the next node, which was saved in temp

        new_head = self.tail   #the tail is now the head
        self.tail = self.head   #the old head is now the new tail
        self.head = new_head    #assign new head

    def dummy_reverse(self):  #reversing with a dummy node(creating a new linked list)
        if self.head is None:   #empty case
            print(f"List does not exist")
            return
        if self.head == self.tail: #single node case
            print(f"Cannot reverse one node!")
            return

        dummy_head = None  #create the dummy head
        curr = self.head    

        while curr:  #loops through the original list
            new_node = Node(curr.data)  #create a new node with the current data
            new_node.next = dummy_head #make new node point to the current dummy head
            
            if dummy_head:  #if the dummy head exists(new head of the reversed list)
                dummy_head.prev = new_node  #update dummy_head's previous pointer 
            
            dummy_head = new_node #move dummy head to the new node
            curr = curr.next
        
        self.head = dummy_head #set the real head to point to the dummy head

        self.tail = self.head  #reverse the tail to the new head
        while self.tail.next:   #traverse to the last node to set the tail 
            self.tail = self.tail.next  #move the tail to the last node

    def print_reverse(self): #does not modify the list, Prints values from tail to head
        if self.head is None:
            print(f"List is empty")
            return
        curr = self.tail
        
        while curr:
            print(curr.data)
            curr = curr.prev


    def delete_node_by_value(self, value):
        if self.head is None:
            print(f"Delete failed, list is empty")
            return
        
        if self.head.data == value:   #deleting the first node
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        
        curr = self.head

        while curr:  #loop to find the node
            if curr.data == value:  #found node to delete
                if curr.next:
                    curr.next.prev = curr.prev #updating pointers
                if curr.prev:
                    curr.prev.next = curr.next
                if curr == self.tail: #if deleting the last node
                    self.tail = curr.prev
                return
            else:
                curr = curr.next

        print(f"Value not found")

    def delete_nth_node_end(self, value):  #go to the tail and count back {value} number of spaces
        if self.head is None:
            print(f"Delete failed, list is empty")
            return
        
        curr = self.tail
        count = 1

        while curr and count < value:  #moving backwards
            curr = curr.prev
            count += 1

        if curr is None:  #traversing past the head(too many)
            print(f"Delete failed, invalid position")
            return
        
        self.delete_node_by_value(curr.data)  #delete the found node

    def sort_and_remove_dups(self): #array sort approach
        if self.head is None:
            print(f"List is empty, no duplicates to remove")
            return
        
        values = []   #empty python list (array) to handle values

        curr = self.head

            # TC - O(n)
        while curr:   #putting everyting in the python list 
            values.append(curr.data)
            curr = curr.next

            #TC - O(nlogn)
        values.sort()  #sorting the python list  (****Tim sort****)

        self.head = None
        last_inserted = None

            #TC - O(n)
        for val in values:
            if self.head is None:   #first value becomes head
                self.insert_head(val)
                last_inserted = val  #update last inserted value
            elif val != last_inserted:  #only insert if different from last inserted value
                self.insert_tail(val)
                last_inserted = val  #update last inserted value

        self.tail = self.head  #start at the head

            #TC - O(n)
        while self.tail and self.tail.next:  #move until the last node
            self.tail = self.tail.next      #traverse forward


################################# Test Cases ###
            
# ============================
# Doubly Linked List - Testing
# ============================

# Create a new doubly linked list
dll = DoublyLinkedList()

# 1. Print empty list
print("1. Printing empty list:")
dll.print_list()
print("-" * 30)

# 2. Insert at head & tail
print("2. Insert at head and tail:")
dll.insert_head(10)
dll.insert_head(5)
dll.insert_tail(20)
dll.insert_tail(30)
dll.print_list()
print("-" * 30)

# 3. Insert at a specific index
print("3. Insert at index 2 (between 10 and 20):")
dll.insert_at(2, 15)
dll.print_list()
print("-" * 30)

# 4. Get values at index
print("4. Get values at specific indices:")
print("Value at index 0:", dll.get_at(0))
print("Value at index 2:", dll.get_at(2))
print("Value at index 4:", dll.get_at(4))
print("Value at index 10 (invalid):", dll.get_at(10))
print("-" * 30)

# 5. Search for values
print("5. Searching for values:")
print("Searching for 10:", dll.search(10))
print("Searching for 25:", dll.search(25))
print("-" * 30)

# 6. Delete at index
print("6. Deleting at index 2 (removing 15):")
dll.delete_at(2)
dll.print_list()
print("-" * 30)

print("6. Deleting at index 0 (removing head):")
dll.delete_at(0)
dll.print_list()
print("-" * 30)

# 7. Get size
print("7. List size:")
print("Size of the list:", dll.size())
print("-" * 30)

# 8. Reverse the list (in-place)
print("8. Reversing the list:")
dll.reverse()
dll.print_list()
print("-" * 30)

# 9. Reverse the list using dummy method
print("9. Dummy Reverse (creates a new reversed list):")
dll.dummy_reverse()
dll.print_list()
print("-" * 30)

# 10. Print the list in reverse order
print("10. Printing list in reverse order:")
dll.print_reverse()
print("-" * 30)

# 11. Delete by value
print("11. Deleting node by value (delete 20):")
dll.delete_node_by_value(20)
dll.print_list()
print("-" * 30)

print("11. Attempting to delete a value not in the list (99):")
dll.delete_node_by_value(99)
print("-" * 30)

# 12. Delete nth node from the end
print("12. Deleting 1st node from the end:")
dll.delete_nth_node_end(1)
dll.print_list()
print("-" * 30)

# 13. Insert duplicate values
print("13. Inserting duplicate values:")
dll.insert_tail(20)
dll.insert_tail(30)
dll.insert_tail(10)
dll.insert_tail(20)
dll.insert_tail(30)
dll.insert_tail(10)
dll.print_list()
print("-" * 30)

# 14. Sort and Remove Duplicates
print("14. Sorting and removing duplicates:")
dll.sort_and_remove_dups()
dll.print_list()
print("-" * 30)