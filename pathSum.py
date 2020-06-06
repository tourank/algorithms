class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value=value 

def pathSum(root, target):

    if root is None:
        return False 
    if sum == root.val and root.left is None and root.right is None:
        return True

    return pathSum(root.left, target-root.value) or pathSum(root.right, target-root.val)

p = Node(5)
a = Node(9)
b = Node(20)
c = Node(15)
d = Node(7)

p.left = Node(4) 
p.right = Node(8) 
Node(4).left = Node(11)
Node(11).left = 7
Node(11).right = 2
Node(8).left = Node(13)
Node(8).right = Node(4)
Node(4).right = Node(1)
print(pathSum(p, 1, 0))
