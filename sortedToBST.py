class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value=value 

def sortedArrayToBST(array):
    if len(array) == 0:
        return None
    return makeTreeNode(array,left,right)

def makeTreeNode(array, left, right):
    mid = (left + right)//2
    if left > right:
        return None
    node = Node(array[mid])
    node.left = makeTreeNode(array, left, mid-1)
    node.right = makeTreeNode(array, mid+1, right)
    return node

def isBalancedBool(root):
    return isBalanced(root, 0, 0)

def computeHeight(root, height):

    if root is None:
        return height
    return max(computeHeight(root.left, height+1), computeHeight(root.right, height+1))

def isBalanced(root, heightLeft, heightRight):

    if root is None:
        return True
    flag = abs( computeHeight(root.left,heightLeft) - computeHeight(root.right, heightRight) ) < 1

    return flag 


a = Node(3)
a.right = Node(20)
a.left = Node(9)
Node(20).left = Node(7)
Node(20).right = Node(15)
Node(15).left = Node(8)
Node(8).left = Node(9)
print(isBalancedBool(a))
