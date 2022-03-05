# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        root = ListNode(0, next=head)
        before = root
        current = head
        first = None        
        before_first = None
        
        while current:
            if current.val >= x and first is None:
                first = current
                before_first = before
                before = before.next
                current = current.next
                
            elif current.val < x and first:
                before.next = current.next
                current.next = first
                before_first.next = current
                before_first = current
                
                current = before.next
                
            else:
                before = before.next
                current = current.next
                
        return root.next
