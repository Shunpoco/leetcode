from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lis = []

        while head is not None:
            lis.append(head.val)
            head = head.next

        l = len(lis)

        r = 0
        for i in range(l//2):
            v = lis[i] + lis[l-1-i]
            if v > r:
                r = v

        return r

