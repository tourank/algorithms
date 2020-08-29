import math 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def getDecimalValue(head):

    ptr = head
    count = 0
    result = 0
    if ptr is not None:
        count = 1

    while ptr.next is not None:
        ptr = ptr.next
        count+=1

    ptr = head 
    count -=1
    while ptr is not None:
        result += int(ptr.val * math.pow(2, count))
        ptr = ptr.next
        count -= 1

    return result


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

print(getDecimalValue(head))
