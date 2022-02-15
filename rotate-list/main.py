# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        r = []
        
        cur = head
        while cur:
            r.append(cur)
            cur = cur.next
            
        
        k %= len(r)
        if k == 0:
            return head

        h = r[len(r)-k]
        
        r[len(r)-k-1].next = None
        r[len(r)-1].next = r[0]
        
        return h
