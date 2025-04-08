class Node:
    def __init__(self, value):  
        self.data = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    
    queue = []
    result = []

    queue.append(root)  #root node goes into the queue

    while queue:    #if the queue is not empty
        current_node = queue.pop(0) #remove the first node from the queue
        print(current_node.data)    #print value and 
        result.append(current_node.data) #add to result list
        
        if current_node.left: #add left child to queue
            queue.append(current_node.left)
        
        if current_node.right: #add right child to the queue
            queue.append(current_node.right)

    return result
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

bfs_result = bfs(root)
print(bfs_result)