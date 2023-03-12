from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.exec(lists)

    def exec(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None
        if n == 1:
            return lists[0]
        
        m = n // 2

        a = self.exec(lists[:m])
        b = self.exec(lists[m:])

        head = ListNode(0)
        cur = head

        while a is not None and b is not None:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next

            cur = cur.next

        while a is not None:
            cur.next = a
            a = a.next
            cur = cur.next

        while b is not None:
            cur.next = b
            b = b.next
            cur = cur.next

        return head.next


