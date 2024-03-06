# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one = head
        two = head

        while one is not None and two is not None:
            one = one.next
            if one is None:
                break

            two = two.next
            if two is None:
                break

            two = two.next
            if two is None:
                break
            elif one == two:
                return True

        return False
