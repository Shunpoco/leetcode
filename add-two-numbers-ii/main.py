from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1, v2 = 0, 0

        nex = l1
        while nex is not None:
            v1 += 1
            nex = nex.next

        nex = l2
        while nex is not None:
            v2 += 1
            nex = nex.next

        if v2 > v1:
            v1, v2 = v2, v1
            l1, l2 = l2, l1

        result = [0 for _ in range(v1)]

        nex = l1
        for i in range(v1):
            result[i] += nex.val
            nex = nex.next

        nex = l2
        for i in range(v2):
            result[i+(v1-v2)] += nex.val
            nex = nex.next

        carry = 0
        for i in range(v1-1, -1, -1):
            if result[i] >= 10:
                if i == 0:
                    carry = 1
                else:
                    result[i-1] += 1
                result[i] -= 10
        if carry == 1:
            v = [carry]
            v.extend(result)
            result = v

        root = ListNode()
        nex = root
        for r in result:
            nex.next = ListNode(r)
            nex = nex.next

        return root.next
