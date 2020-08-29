class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum(root, L, R, sigma):
    
    if root is None:
        return 0 
    if root.val >= L and root.val <= R:
        sigma = root.val
        return sigma + range_sum(root.left, L, R, sigma) + range_sum(root.right, L, R, sigma)

    return range_sum(root.left, L, R, sigma) + range_sum(root.right, L, R, sigma)


x = Node(10)
x.left = Node(11)
print(range_sum(x, 5, 15, 0))

