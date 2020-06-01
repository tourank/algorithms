class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value=value 

def insert(root, value):
    if root is None:
        node = Node(value)
        root = node
    elif value < root.value:
        root.left = insert(root.left, value)
    elif value >= root.value:
        root.right = insert(root.right, value)
    return root
    
def dfs(root):
    if root is None:
        return
    else:
        print(root.value)
        dfs(root.right)
        dfs(root.left)

def closestValue(root, target):
    closestVal = root.value
    return helper(root, target, closestVal)
def helper(tree, target, closestValue):
    if tree is None:
        return closestValue
    if abs(tree.value - target) < abs(closestValue - target):
        closestValue = tree.value
    if target < tree.value:
        return helper(tree.left, target, closestValue)
    elif target > tree.value:
        return helper(tree.right, target, closestValue)
    else:
        return closestValue

def isSameTree(p, q):

    if p is None and q is None:
        return True
    elif p is None and q is not None:
        return False
    elif p is not None and q is None:
        return False
    if p.value != q.value:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def symmetricTree(root):
    list1 = []
    list2 = []
    dfs_right(root, list1)
    dfs_left(root, list2)
    return list1 == list2

def dfs_right(root, list1):
    if root is None:
        list1.append(None)
        return
    list1.append(root.value)
    dfs_right(root.right, list1)
    dfs_right(root.left, list1)

def dfs_left(root, list2):

    if root is None:
        list2.append(None)
        return
    list2.append(root.value)
    dfs_left(root.left, list2)
    dfs_left(root.right, list2)

def maxDepthCall(root):
    depth = 0
    maximum = 0
    return maxDepth(root, depth, maximum)

def maxDepth(root, depth, maximum):
    # depth = depth(root.left, depth+1) + depth(root.right, depth+1)
    if root is None:
        return depth

    #if depth > maximum:
        #maximum = depth
 
    return max(maxDepth(root.left,depth+1,maximum), maxDepth(root.right, depth+1, maximum))
    
    
p = Node(3)
a = Node(9)
b = Node(20)
c = Node(15)
d = Node(7)

p.left = a 
p.right = b
b.left = c
b.right = d

print(maxDepthCall(p))
