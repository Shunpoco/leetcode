# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        tail = None
        cur = head
        while cur is not None:
            tail = cur
            cur = cur.next

        n = 1
        prev = None
        t = tail
        cur = head
        while cur != tail:
            if n % 2 == 1:
                prev = cur
            else:
                t.next = cur
                t = cur
                prev.next = cur.next
            n += 1
            cur = cur.next

        if n % 2 == 0:
            t.next = cur
            t = cur
            prev.next = cur.next

        if t is not None:
            t.next = None
        return head
