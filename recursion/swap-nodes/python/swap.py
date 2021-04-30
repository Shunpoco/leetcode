class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        nn = self.swapPairs(head.next.next)

        h = head
        n = head.next

        n.next = h
        h.next = nn
        head = n

        return head
