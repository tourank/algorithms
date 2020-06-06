class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value=value 

def computeDepth(node, height):

    if node is None:
        return height
    return max(computeDepth(node.left, height+1), computeDepth(node.right, height+1)) 

def computeHeight(node):
    if node is None:
        return 0
    left = computeHeight(node.left)
    right= computeHeight(node.right)
    if abs(left - right) > 1:
        return -1
    return max(computeHeight(node.left), computeHeight(node.right)) + 1

def balancedTree(node):

    if node is None:
        return True
    if computeHeight(node) > 1:
        return False
    return True


p = Node(1)
a = Node(2)
b = Node(3)
c = Node(15)
d = Node(7)

p.right= a
a.right = Node(3)
#print(balancedTree(p))
print(computeHeight(p))
