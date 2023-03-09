# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash = defaultdict(int)
        while True:
            if head is None:
                return None
            hash[head] += 1
            if hash[head] == 2:
                break
            head = head.next

        return head

