from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        pos = 1
        prev = None
        
        while pos < left:
            prev = cur
            cur = cur.next
            pos += 1
            
        stack = []
        
        while pos <= right:
            stack.append(cur)
            cur = cur.next
            pos += 1
            
        while len(stack) > 0:
            n = stack.pop()
            
            if prev:
                prev.next = n
            else:
                head = n
            prev = n
            prev.next = None
            
        if cur:
            prev.next = cur
        
        return head
