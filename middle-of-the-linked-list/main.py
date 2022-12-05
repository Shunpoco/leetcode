# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        l = 0
        cur = head
        while cur is not None:
            l += 1
            cur = cur.next
            
        m = l // 2
        
        cur = head
        i = 0
        while i < m:
            i += 1
            cur = cur.next
            
        return cur
