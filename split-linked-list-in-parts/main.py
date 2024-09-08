# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        cur = head

        while cur is not None:
            l += 1
            cur = cur.next

        ls = [l//k for _ in range(k)]
        for i in range(l%k):
            ls[i] += 1

        result = [None for _ in range(k)]
        cur = head
        idx = 0
        while cur is not None:
            result[idx] = cur
            for i in range(ls[idx]):
                t = cur
                cur = cur.next
                if i == ls[idx]-1:
                    t.next = None

            idx += 1

        return result

