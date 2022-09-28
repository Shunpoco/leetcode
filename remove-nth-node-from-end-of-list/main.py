from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_nodes = self.get_nodes(head)
        
        h = ListNode(val=-1, next=head)
        cur = h
        i = 0
        target = n_nodes - n
        
        while True:
            if i == target:
                # nextがremoveすべきnode
                next_node = cur.next
                nn_node = next_node.next    
                cur.next = nn_node
                break
            i += 1
            cur = cur.next
            
        return h.next
        
        
    def get_nodes(self, head: Optional[ListNode]) -> int:
        n = 0
        
        while head:
            n += 1
            head = head.next
            
        return n
