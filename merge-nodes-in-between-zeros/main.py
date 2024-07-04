# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        c = result

        nex = ListNode(val=0)

        cur = head
        while cur is not None:
            if cur.val == 0:
                if c is None:
                    c = nex
                    result = nex
                else:
                    c.next = nex
                    c = c.next
                nex = ListNode(val=0)
            else:
                nex.val += cur.val

            cur = cur.next

        return result.next
