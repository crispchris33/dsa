# ==============================
# Binary Search Tree (BST) Methods
# ==============================

# Insert Methods
# --------------------------------
# insert(value)                → Inserts a node into the BST (iteratively).
# insert_recursive(root, value) → Inserts a node recursively into the BST.

# Search Methods
# --------------------------------
# search(value)                → Searches for a value in the BST (iteratively), returns True/False.
# search_recursive(root, value) → Searches for a value recursively in the BST.

# Traversal Methods
# --------------------------------
# preorder_traversal(root)  → Preorder traversal (Root → Left → Right).
# inorder_traversal(root)   → Inorder traversal (Left → Root → Right, sorted order).
# postorder_traversal(root) → Postorder traversal (Left → Right → Root).
# level_order_traversal(root) → Level-order (BFS) traversal using a queue.

# Deletion Methods
# --------------------------------
# delete(value)            → Deletes a node from the BST (iterative approach).
# delete_recursive(root, value) → Deletes a node recursively from the BST.

# Utility Methods
# --------------------------------
# find_min(root) → Finds the minimum value node in a subtree.
# find_max(root) → Finds the maximum value node in a subtree.
# height(root)   → Returns the height of the BST.
# size(root)     → Returns the number of nodes in the BST.
# is_balanced(root) → Checks if the BST is height-balanced.

# Successor & Predecessor
# --------------------------------
# find_successor(value)   → Finds the inorder successor of a given value.
# find_predecessor(value) → Finds the inorder predecessor of a given value.

# Additional Methods
# --------------------------------
# invert_tree(root) → Inverts the BST (swaps left and right children recursively).


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    #insert methods
        
    def insert(self, value):    #standard insert method
        if self.root is None:  #checking if the tree is empty
            self.root = Node(value)   #creating node and assiging root
            return
        
        curr = self.root

        while curr:             #loop to find a spot to insert
            if value < curr.data:   #insert in the left side
                if curr.left is None:
                    curr.left = Node(value)
                    return
                else:
                    curr = curr.left

            else:               #inserting on the right
                if curr.right is None:
                    curr.right = Node(value)
                    return
                else:
                    curr = curr.right

    def insert_recursive(self, root, value):
        if root is None:            #base case, empty, create new node
            return Node(value)
        
        if value < root.data:   #inserting in the left subtree
            root.left = self.insert_recursive(root.left, value)
        else:                   #inserting in the right subtree
            root.right = self.insert_recursive(root.right, value)

        return root  

    #search methods
    #search functions are to find one value  O(n) - O(Log n)
        
    def search(self, value):  
        curr = self.root        #start searching from the root

        while curr:     #loop until finding the value or reaching the end
            if value == curr.data:      #found the value
                return True
            elif value < curr.data:     #if the value is smaller, move to the left side
                curr = curr.left
            else:                   #if the value is larger, move to the right
                curr = curr.right

        return False  #not found

    def search_recursive(self, root, value):  #O(n) - O(Log n)
        if root is None:            #if the root is empty, value not found
            return False
        
        if value == root.data:      #found the value sequence
            return True
        elif value < root.data:     #if the value is smaller go to the left side
            return self.search_recursive(root.left, value)
        else:                       #if the value is larger, go to the right side
            return self.search_recursive(root.right, value)

    #Traverse Methods
        #traverse methods are to output the entire tree
        
    def preorder_traversal(self, root):    #root > left > right
        if root is None:     #empty tree
            return
        
        print(root.data)

        self.preorder_traversal(root.left)      #recursively left subtree
        self.preorder_traversal(root.right)     #recursiverly right subtree
    
    def inorder_traversal(self, root):      #left > root > right
        if root is None:     #empty tree
            return
        
        self.inorder_traversal(root.left)           #recursively left subtree
        print(root.data)                            #root
        self.inorder_traversal(root.right)          #recursively right subtree

    def postorder_traversal(self, root):      #left > right > root
        if root is None:     #empty tree
            return
        
        self.postorder_traversal(root.left)           #recursively left subtree
        self.postorder_traversal(root.right)          #recursively right subtree
        print(root.data)                            #root

    def level_order_traversal(self, root):
        if root is None:     #empty tree
            return
        
        queue = []         #create empty queue to store nodes at each level
        queue.append(root)          #add root to the queue

        while queue:        #loop through nodes
            curr = queue.pop(0)     #remove the front node from the queue
            print(curr.data)        #print the current node

            if curr.left:       #if the left child exists - pop it
                queue.append(curr.left)
        
            if curr.right:      #if the right child exists - pop it
                queue.append(curr.right)


    #Deletion Methods
        
    def delete(self, value):
        curr = self.root  #start searching from root
        parent = None     #track parent node

        while curr and curr.data != value:      #search for the node
            parent = curr
            if value < curr.data:       #move left
                curr = curr.left
            else:                       #move right
                curr = curr.right

        if curr is None:            #value not found
            return
        
        #case 1 - no children
        if curr.left is None and curr.right is None:    #if deleting root node
            if curr == self.root:
                self.root = None
            elif curr == parent.left:
                parent.left = None
            else:
                parent.right = None

        #case 2 - one child - right
        elif curr.left is None:
            if curr == self.root:
                self.root = curr.right
            elif curr == parent.left:
                parent.left = curr.right
            else:
                parent.right = curr.right
        
        #case 3 - one child - left
        elif curr.right is None:
            if curr == self.root:
                self.root = curr.left
            elif curr == parent.left:
                parent.left = curr.left
            else:
                parent.right = curr.left

        #case 3 - two children
        else:
            successor_parent = curr
            successor = curr.right

            while successor.left:       #find the inorder successor - smallest in right subtree
                successor_parent = successor
                successor = successor.left

            curr.data = successor.data  #copy successor data to current node

            #delete successor - at most 1 right child
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right


    def delete_recursive(self, root, value):
        if root is None:     #empty tree
            return
        
        if value < root.data:       #search in the left subtree
            root.left = self.delete_recursive(root.left, value)

        elif value > root.data:     #search in the right subtree
            root.right = self.delete_recursive(root.right, value)

        else:   #node to delete found
            #case 1 and 2 - node has 1 child or no child
            if root.left is None:
                return root.right   #return the right child or none
            
            elif root.right is None:
                return root.left    #return the left child
            
            #case 3 - node has 2 children
            successor = self.find_min(root.right)   #find in-order successor
            root.data = successor.data              #replace the node's value with successor's value
            root.right = self.delete_recursive(root.right, successor.data)  #delete successor node

        return root     #return the updated tree

    #Utility Methods

    def find_min(self, root):  #the minimum value is the leftmost node
        while root.left:
            root = root.left
        return root
        
    def find_max(self, root):
        while root.right:       #traverse right side
            root = root.right
        return root     #rightmost node is the max value

    def height(self, root):
        if root is None:  #if the tree is empty
            return -1
        
        left_height = self.height(root.left)  #Compute the height of the left subtree
        right_height = self.height(root.right) #Compute the height of the right subtree

        #The height of the tree is the maximum depth of its left or right... 
        #... subtree plus 1 (for the current node).
        return max(left_height, right_height) + 1

    def size(self, root):
        if root is None:  #if the tree is empty
            return 0
        
        left_size = self.size(root.left) #compute the size of the left side
        right_size = self.size(root.right) #compute the size of the right side

        return left_size + right_size + 1  #add the sizes of the 2 sides plus the root node

    def is_balanced(self, root):
        if root is None:  #if the tree is empty
            return True
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:  #height difference check
            return False
        
        return self.is_balanced(root.left) and self.is_balanced(root.right) #recursive traversal

    #Additional Methods
        
    def find_successor(self, value):
        curr = self.root
        
        while curr:         #standard BST search loop
            if value == curr.data:
                break   #found node target - exit loop
            elif value < curr.data:
                curr = curr.left  #move left to smaller values
            else:
                curr = curr.right #move right to larer values

        if curr is None: #value is not found in the BST, return none
            return None
        
            #case 1 - node has a right subtree
        if curr.right:   #if the node has a right subtree
            return self.find_min(curr.right)   #the successor is the smallest node in the right
        
            #case 2 - no right subtree - find lowest ancestor whose left child is ancestor of target
        else:
            successor = None
            ancestor = self.root

            while ancestor:
                if value < ancestor.data:     #move left, track potential successor
                    successor = ancestor
                    ancestor = ancestor.left
                elif value > ancestor.data:    #move right
                    ancestor = ancestor.right
                else:
                    break  #found target

        return successor

    def find_predecessor(self, value):
        curr = self.root

            #step 1 - locate the target node
        while curr:
            if value == curr.data:
                break
            elif value < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:  #if value not found
            return None

            #step 2
        if curr.left:       #if node has a left subtree, find the max 
            return self.find_max(curr.left)
        
        predecessor = None  #step 3 - if no left subtree, find the lowest ancestor that is smaller
        ancestor = self.root

        while ancestor:
            if value > ancestor.data:   #move right and track potential predecessor
                predecessor = ancestor
                ancestor = ancestor.right
            elif value < ancestor.data: #move left
                    ancestor = ancestor.left
            else:
                break #found target and break the loop

        return predecessor

    def invert_tree(self, root):
        if root is None:
            return None
        
        temp = root.left    #assign left to a temp node
        root.left = root.right  #switch right node to the left node
        root.right = temp       #assign the right node to the old left value which was held at temp

        self.invert_tree(root.left) #recursive repeat through the left side
        self.invert_tree(root.right)    #recursive repeat through the right side
        return root     #return the tree
    

# Create an instance of BinaryTree
bst = BinaryTree()

# 1. Inserting values
print("1. Inserting values:")
values = [10, 5, 15, 3, 7, 12, 18]
for val in values:
    bst.insert(val)
print("Inserted:", values)
print("-" * 30)

# 2. Searching for values
print("2. Searching for values:")
print("Searching for 7:", bst.search(7))   # Expected: True
print("Searching for 20:", bst.search(20)) # Expected: False
print("-" * 30)

# 3. Recursive Search for values
print("3. Recursive Search for values:")
print("Searching for 12:", bst.search_recursive(bst.root, 12)) # Expected: True
print("Searching for 8:", bst.search_recursive(bst.root, 8))   # Expected: False
print("-" * 30)

# 4. Preorder Traversal (Root-Left-Right)
print("4. Preorder Traversal (Root-Left-Right):")
bst.preorder_traversal(bst.root)
print("-" * 30)

# 5. Inorder Traversal (Left-Root-Right - Sorted Order)
print("5. Inorder Traversal (Left-Root-Right - Sorted Order):")
bst.inorder_traversal(bst.root)
print("-" * 30)

# 6. Postorder Traversal (Left-Right-Root)
print("6. Postorder Traversal (Left-Right-Root):")
bst.postorder_traversal(bst.root)
print("-" * 30)

# 7. Level Order Traversal (Breadth-First Search)
print("7. Level Order Traversal (Breadth-First Search):")
bst.level_order_traversal(bst.root)
print("-" * 30)

# 8. Finding Min & Max
print("8. Finding Min & Max:")
print("Min Value in BST:", bst.find_min(bst.root).data)  # Expected: 3
print("Max Value in BST:", bst.find_max(bst.root).data)  # Expected: 18
print("-" * 30)

# 9. Height of the Tree
print("9. Height of the Tree:")
print("Tree Height:", bst.height(bst.root))  # Expected: 2
print("-" * 30)

# 10. Size of the Tree (Number of Nodes)
print("10. Size of the Tree (Number of Nodes):")
print("Tree Size:", bst.size(bst.root))  # Expected: 7
print("-" * 30)

# 11. Checking if Tree is Balanced
print("11. Checking if Tree is Balanced:")
print("Is Balanced:", bst.is_balanced(bst.root))  # Expected: True (Depends on Insert Order)
print("-" * 30)

# 12. Finding Successor & Predecessor
print("12. Finding Successor & Predecessor:")
print("Successor of 10:", bst.find_successor(10).data if bst.find_successor(10) else None)  # Expected: 12
print("Predecessor of 10:", bst.find_predecessor(10).data if bst.find_predecessor(10) else None)  # Expected: 7
print("-" * 30)

# 13. Deleting a Leaf Node (7)
print("13. Deleting a Leaf Node (7):")
bst.delete(7)
print("Inorder Traversal after deleting 7:")
bst.inorder_traversal(bst.root)
print("-" * 30)

# 14. Deleting a Node with One Child (5)
print("14. Deleting a Node with One Child (5):")
bst.delete(5)
print("Inorder Traversal after deleting 5:")
bst.inorder_traversal(bst.root)
print("-" * 30)

# 15. Deleting a Node with Two Children (10 - Root)
print("15. Deleting a Node with Two Children (10 - Root):")
bst.delete(10)
print("Inorder Traversal after deleting 10:")
bst.inorder_traversal(bst.root)
print("-" * 30)

# 16. Recursive Deletion (Removing 12)
print("16. Recursive Deletion (Removing 12):")
bst.root = bst.delete_recursive(bst.root, 12)
print("Inorder Traversal after recursive deletion of 12:")
bst.inorder_traversal(bst.root)
print("-" * 30)

# 17. Inverting the Binary Tree
print("17. Inverting the Binary Tree:")
bst.invert_tree(bst.root)
print("Inorder Traversal after tree inversion:")
bst.inorder_traversal(bst.root)
print("-" * 30)