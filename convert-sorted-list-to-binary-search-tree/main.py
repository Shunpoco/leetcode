from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []

        while head is not None:
            nodes.append(head.val)
            head = head.next


        return self.exec(nodes)

    def exec(self, nodes: List[int]) -> TreeNode:
        if len(nodes) == 0:
            return None

        m = len(nodes) // 2

        return TreeNode(
            nodes[m],
            self.exec(nodes[0:m]),
            self.exec(nodes[m+1:len(nodes)]),
        )

