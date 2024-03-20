# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        n = 0

        head = list1
        c = 0
        while c < a-1:
            c += 1
            head = head.next

        nn = head.next
        c += 1
        head.next = list2

        while c <= b:
            c += 1
            nn = nn.next

        h2 = list2
        while h2.next is not None:
            h2 = h2.next

        h2.next = nn

        return list1
