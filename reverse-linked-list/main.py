# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head is not None:
            stack.append(head)
            head = head.next

        head = ListNode()
        t = head
        for i in range(len(stack)-1, -1, -1):
            v = stack[i]
            v.next = None
            t.next = v
            t = t.next

        return head.next
