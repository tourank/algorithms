class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    # create helper that takes "total" as argument 
    total = 0
    array = []
    return helper(root, total, array)

def helper(root, total, array):

    if root is None:
        array.append(total)
    return array


