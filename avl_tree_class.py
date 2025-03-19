class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)
        
        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
    
            #calculate the height root + tallest branch
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) 

        balance = self.get_height(root.left) - self.get_height(root.right)

        if balance > 1 and value < root.left.data:
            return self.right_rotate(root)
        
        if balance < -1 and value > root.right.data:
            return self.left_rotate(root)
        
        if balance > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
        
    def get_height(self, node):   #returns node height attribute
        if node is None:   #empty node is height zero
            return 0
        return node.height
    
    def left_rotate(self, z):  #if the right side is heavy, rotate the tree left
        y = z.right   #make right child new root
        T2 = y.left     #left subtree of y is stored

        y.left = z  #move z down
        z.right = T2    #move T2 to z's right

            #update heights of all nodes recursively 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y    #return the new root

    def right_rotate(self, z):  #if the left side is heavy, rotate the tree right
        y = z.left      #make left child new root
        T3 = y.right    #store right subtree of y

        y.right = z     #move z down and y becomes the new root
        z.left = T3     #move T3 to z's left (reconnect the subtree)

            #reassign node height attributes recursively 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def delete(self, root, value):
        if root is None:
            return None
        
            #recursive search for the particular node
        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            #case 1 - no children
            if root.left is None and root.right is None:
                return None
            
            #case 2 - 1 child
            if root.left is not None and root.right is None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            
            #case 3 - 2 children
            successor = self.find_min(root.right)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_height(root.left) - self.get_height(root.right)

        if balance > 1:   #left heavy
            if self.get_height(root.left.left) >= self.get_height(root.left.right):
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:   #right heavy
            if self.get_height(root.right.right) >= self.get_height(root.right.left):
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root
    
    #to find the successor to the root - used in delete method
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

        #find node by value
    def search(self, value):
        if self.root is None:
            return False
        
        curr = self.root   #start at root

        while curr:
            if value == curr.data:
                return True
            elif value < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return False
    

# Create an instance of AVLTree
avl = AVLTree()

# 1. Inserting values
print("1. Inserting values:")
values = [10, 5, 15, 3, 7, 12, 18]
for val in values:
    avl.root = avl.insert(avl.root, val)
print(values)
print("-" * 30)

# 2. Searching for values
print("2. Searching for values:")
print(avl.search(7))
print(avl.search(20))
print("-" * 30)

# 3. Deleting a value
print("3. Deleting a value:")
avl.root = avl.delete(avl.root, 7)
print(avl.search(7))
print("-" * 30)

# 4. Inserting duplicates
print("4. Inserting duplicates:")
duplicate_values = [10, 12]
for val in duplicate_values:
    avl.root = avl.insert(avl.root, val)
print(duplicate_values)
print(avl.search(10))
print(avl.search(12))
print("-" * 30)

# 5. Finding the minimum value in the tree
print("5. Finding the minimum value in the tree:")
min_node = avl.find_min(avl.root)
if min_node:
    print(min_node.data)
else:
    print("None")
print("-" * 30)

# 6. Deleting the minimum value found
print("6. Deleting the minimum value found:")
if min_node:
    avl.root = avl.delete(avl.root, min_node.data)
    new_min = avl.find_min(avl.root)
    if new_min:
        print(new_min.data)
    else:
        print("None")
else:
    print("None")
print("-" * 30)

# 7. Final searches
print("7. Final searches:")
print(avl.search(15))
print(avl.search(7))
print("-" * 30)
