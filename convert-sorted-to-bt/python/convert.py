from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next

        return self._tree(l)


    def _tree(self, nodes: List[int]) -> TreeNode:
        if len(nodes) == 0:
            return None

        m = int(len(nodes)/2)

        r = TreeNode(nodes[m])

        r.left = self._tree(nodes[:m])
        r.right = self._tree(nodes[m+1:])

        return r
