# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        i1, i2 = head, head.next
        if i2 is None:
            return False

        while i1 != i2:
            i1 = i1.next
            i2 = i2.next
            if i1 is None or i2 is None:
                return False
            i2 = i2.next

            if i2 is None:
                return False

        return True

