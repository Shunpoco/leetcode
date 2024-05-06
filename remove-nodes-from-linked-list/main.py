# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head


        while cur is not None:
            while len(stack) > 0 and stack[-1].val < cur.val:
                stack.pop(-1)
                if len(stack) > 0:
                    stack[-1].next = cur

            stack.append(cur)
            cur = cur.next

        return stack[0]

