# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        l = []
        i = 0
        n = len(traversal)

        while i < n:
            d = 0
            while i < n and traversal[i] == '-':
                d += 1
                i += 1

            v = 0
            while i < n and traversal[i].isdigit():
                v = v * 10 + int(traversal[i])
                i += 1

            node = TreeNode(v)

            if d < len(l):
                l[d] = node
            else:
                l.append(node)

            if d > 0:
                parent = l[d-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        return l[0]
