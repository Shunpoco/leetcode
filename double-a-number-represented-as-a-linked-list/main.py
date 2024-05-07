# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur is not None:
            stack.append(cur)
            cur = cur.next

        co = 0
        while len(stack) > 0:
            node = stack.pop(-1)

            v = (node.val * 2 + co)

            if v > 9:
                co = 1
            else:
                co = 0

            node.val = v % 10

            if len(stack) == 0 and co == 1:
                zero = ListNode(1, head)
                head = zero

        return head
            



