# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []

        next = head

        while next is not None:
            stack.append(next)
            next = next.next

        b = None
        for i in range(len(stack)-1, -1, -1):
            n -= 1
            if n == 0:
                continue
            v = stack[i]
            v.next = b
            b = v

        return b
