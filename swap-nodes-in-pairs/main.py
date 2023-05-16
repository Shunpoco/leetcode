from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        self.swap(head, dummy)

        return dummy.next


    def swap(self, node: Optional[ListNode], par: ListNode):
        if node is None or node.next is None:
            return

        child = node.next
        grandchild = child.next
        par.next = child
        child.next = node
        node.next = grandchild

        self.swap(grandchild, node)

