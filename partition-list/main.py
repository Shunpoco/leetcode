# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy  = ListNode(-300, head)
        prev = dummy
        target_prev = None
        target_node = None

        cur = head

        while cur is not None:
            next_prev = cur
            next_node = cur.next
            if cur.val >= x and target_node is None:
                target_node = cur
                target_prev = prev

            elif cur.val < x and target_node is not None:
                prev.next = cur.next
                target_prev.next = cur
                target_prev = cur
                cur.next = target_node
                next_prev = prev

            prev = next_prev
            cur = next_node

        return dummy.next
