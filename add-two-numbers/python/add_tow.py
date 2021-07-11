# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = None
        n = None
        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            v = v1 + v2 + carry
            if v > 9:
                carry = 1
                v -= 10
            else:
                carry = 0
                
            if n:
                n.next = ListNode(v)
                n = n.next
            else:
                result = ListNode(v)
                n = result
        
        if carry > 0:
            n.next = ListNode(carry)
        
        return result
