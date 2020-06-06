class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value=value 

def invertTree(root):
    
    invertTree(root.left)
    invertTree(root.right)
    if root.left is not None or root.right is not None:
        tmp = root.left.value  
        root.left.value = root.right.value
        root.right.value = tmp

root = Node(4)
root.left = Node(2)
root.right = Node(7)
Node(2).left = Node(1)
Node(2).right = Node(3)
Node(7).left = Node(6)
Node(7).right = Node(9)
