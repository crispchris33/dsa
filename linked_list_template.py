#create node class first with data and next params

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


#create the linked list class
class LinkedList:

    def __init__(self):  #initialize with empty header
        self.head = None

    def insert_head(self, value):  
        #create a new node with value, 
        #set before current head, 
        #update head to new node 

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, value):
        #create new node
        #if head is empty 
        #set head to new node, return
        #else
        #traverse to last node
        #set last node's current point to new node

        new_node = Node(value)
        if self.head is None: #if head is empty part
            self.head = new_node
            return
        else: #if the head is not empty
            curr = self.head  #variable equal to the head node
            while curr.next is not None: #while loop to traverse to the end
                curr = curr.next #traverse action 
                
            curr.next = new_node #last nodes pointer to new node we are creating
    
    def insert_at(self, index, value):
        if index == 0:    #if not populated just revert to insert head function
            self.insert_head(value)
            return
        
        new_node = Node(value) #create node, 
        curr = self.head #set curr at head and count 0 to use in the loop
        count = 0
        
        #loop through to get to the index
        while curr is not None and count < (index - 1): 
            count += 1
            curr = curr.next

        if curr is None:
             #if trying to insert at index that doesnt exist
            return print('Insert at failed, invalid insert index')
        else:
            new_node.next = curr.next
            curr.next = new_node

    def delete_at(self, index):
        if self.head is None:
            return print('Delete at failed, list is empty')
        
        if index == 0: #deleting the first node - 0
            self.head = self.head.next #assign the current head to the head next
            return
        
        curr = self.head #starting point variable
        count = 0 

        while curr.next is not None and count < (index - 1):
            curr = curr.next #iteration action
            count += 1

        if curr is None or curr.next is None:
            #if trying to delete invalid index
            return print('Delete at failed, invalid delete index')
        else: #get to the place 1 before the desired node 
            curr.next = curr.next.next #and assign the pointer 2 spots forward to leave out the current

    def search(self, value): #returns T/F if a value match is found
        curr = self.head  #create start point at header

        while curr is not None: 
            if curr.data == value:  #if curr is equal to the desired value
                return True
            else:
                curr = curr.next #move to next node
        return False

    def get_at(self, index):  #return data from index position
        curr = self.head #start at head
        counter = 0
        while curr is not None:
            if counter == index:
                return curr.data  #return data
            curr = curr.next  #traverse
            counter += 1
        return None

    def print_list(self):  #prints list data
        if self.head is None:
            return print("Empty List") 
    
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next #move to next node

    def size(self):  #returns the size of the list
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def reverse(self): #reverse list order
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next #stores reference to the next node
            curr.next = prev #reverses the link
            prev = curr #move prev forward
            curr = next_node #move curr forward
        self.head = prev #assigns new head

    def delete_node_by_value(self, value):
        if self.head is None:
            return print('Delete node by value failed, list is empty')
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        curr = self.head
        found = False

        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                found = True
                return
            else:
                curr = curr.next

        if not found:
            print(f"Value: {value} not found!")

    def delete_nth_node(self, value):#delete from the end
        size = self.size()
        delete_point = size - value

        if value > size or value <= 0:
            print(f"Invalid delete point.")
            return
        self.delete_at(delete_point)
        print(f"Deleted node at position {value} from the end.")


    def sort_and_remove_dups(self): 
        if self.head is None:
            return print('No duplicates as list is empty')
        
        values = []  #create empty python list
        curr = self.head

        #while there is a list, add values to python list
        while curr is not None:
            values.append(curr.data)
            curr = curr.next

        #sort values in python list
        values.sort()

        #reset the linked list
        self.head = None

        #insert python list values back into the linked list
        for val in values:
            self.insert_tail(val)

        curr = self.head #resetting curr for reorganized list

        while curr and curr.next: 
            if curr.data == curr.next.data: #duplicate check
                curr.next = curr.next.next  #removing dup from curr.next
            else:
                curr = curr.next


#########################################
                
# Create a new LinkedList
linked_list = LinkedList()

# Print the empty list
linked_list.print_list()  

# Insert elements
linked_list.insert_head(10)
linked_list.insert_head(5)
linked_list.insert_tail(20)
linked_list.insert_tail(30)
linked_list.print_list()

# Insert at specific index
linked_list.insert_at(2, 15)
linked_list.print_list()

# Get values at index
print(linked_list.get_at(0))  
print(linked_list.get_at(2))  
print(linked_list.get_at(4))  
print(linked_list.get_at(10)) 

# Search for values
print(linked_list.search(10))  
print(linked_list.search(25))  

# Delete at index
linked_list.delete_at(2)
linked_list.print_list()
linked_list.delete_at(0)
linked_list.print_list()

# Get size
print(linked_list.size())  

# Reverse the list
linked_list.reverse()
linked_list.print_list()

#delete specific value
linked_list.delete_node_by_value(99)
linked_list.delete_node_by_value(12)
linked_list.delete_node_by_value(10)

linked_list.print_list()

linked_list.insert_tail(50)
linked_list.insert_tail(70)
linked_list.insert_tail(15)
linked_list.insert_tail(22)

linked_list.delete_nth_node(2)
linked_list.print_list()

linked_list.delete_nth_node(1)
linked_list.print_list()

linked_list.insert_tail(22)
linked_list.insert_tail(70)
linked_list.insert_tail(22)
linked_list.insert_tail(70)

print("\nPrinting all Before sorting and removing duplicates:")

linked_list.print_list()

print("\nAfter removing duplicates:")

linked_list.sort_and_remove_dups()
linked_list.print_list()
