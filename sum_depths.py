class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    queue = []
    queue.append(root)
    total = 0
    depth = 0
    while(len(queue)>0):
        cur = queue.pop(0)
        total += depth 
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
        depth+=1


