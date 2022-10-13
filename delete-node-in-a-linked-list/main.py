# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        nex = cur.next
        while nex.next is not None:
            cur.val = nex.val
            cur = nex
            nex = cur.next
            
        cur.val = nex.val
        cur.next = None
