from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum = ListNode(-1, head)
        
        _, par1, par2 = self.swap(dum, 0, k, None)

        if par1 == par2:
            return head

        t = par1.next
        par1.next = par2.next
        par2.next = t
        t2 = t.next
        t.next = par1.next.next
        par1.next.next = t2

        return dum.next


    def swap(self, node: Optional[ListNode], idx: int, k: int, parent: Optional[ListNode]) -> Tuple[int, ListNode, ListNode]:
        if  node is None:
            return 0, None, None

        b, par1, par2 = self.swap(node.next, idx+1, k, node)

        if idx == k:
            par1 = parent

        if b == k:
            par2 = node

        return b+1, par1, par2
