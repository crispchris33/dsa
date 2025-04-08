class Node:
    def __init__(self, value):  
        self.data = value
        self.left = None
        self.right = None

def dfs(root):
    if root is None:
        return
    
    stack = []
    result = []

    stack.append(root)

    while stack:
        current_node = stack.pop() #stack - popping top of the stack
        print(current_node.data)
        result.append(current_node.data)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

dfs_result = dfs(root)
print(dfs_result)