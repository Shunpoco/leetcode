# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        
        cur = head
        l = 0
        idx = 0
        tail = None
        tail2 = None
        prev = None
        while True:
            if idx == k:
                idx = 0
                if tail2:
                    tail2.next = prev
                prev = None
                l += 1
                if length - l*k < k:
                    tail.next = cur
                    break
            if idx+1 == k:
                if l == 0:
                    head = cur
                
            if idx == 0:
                tail2 = tail
                tail = cur
                
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
            idx += 1
            
        return head
