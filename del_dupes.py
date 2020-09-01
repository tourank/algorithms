class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Part 1
def delete_duplicates(head):

    if head.next is None:
        return head
    elif head.val == head.next.val:
        head.next = head.next.next
        delete_duplicates(head)
    else:
        delete_duplicates(head.next)

# Part 2 
