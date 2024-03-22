# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        stack = []

        while head is not None:
            v = head.val
            stack.append(v)
            head = head.next

        for i in range(len(stack) // 2):
            if stack[i] != stack[len(stack)-1-i]:
                return False

        return True
