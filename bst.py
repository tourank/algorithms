class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key 

def insert(root, key):
    if root is None:
        node = Node(key)
        root = node
    elif key < root.key:
        root.left = insert(root.left, key)
    elif key >= root.key:
        root.right = insert(root.right, key)
    return root
    
def dfs(root):
    if root is None:
        return
    else:
        print(root.key)
        dfs(root.left)
        dfs(root.right)

def closestValue(root, target):
    if root.left is None or root.right is None:
        print(root.key)
    elif target < root.key:
        closestValue(root.left, target)
    elif target > root.key:
        closestValue(root.right, target)
    else:
        print(root.key)


r = Node(10)
insert(r, 5)
insert(r,15) 
insert(r,2) 
insert(r,5) 
insert(r,1) 
insert(r,13)
insert(r,14)
insert(r,22)
#dfs(r)
closestValue(r,12)
