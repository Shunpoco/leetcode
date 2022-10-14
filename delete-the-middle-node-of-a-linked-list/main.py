from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.length(head)
        
        m = l//2
        
        c = 0
        
        dummy = ListNode(0, head)
        cur = dummy
        while c < m:
            c += 1
            cur = cur.next
            
        cur.next = cur.next.next
        
        return dummy.next
        
        
    def length(self, head: Optional[ListNode]) -> int:
        l = 0
        
        while head is not None:
            l += 1
            head = head.next
            
        return l
