# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            r = TreeNode(val, root, None)

            return r

        queue = [(root, 1)]

        while queue:
            node, d = queue.pop(0)

            if d + 1 == depth:
                left = TreeNode(val, node.left, None)
                right = TreeNode(val, None, node.right)

                node.left = left
                node.right = right

            if node.left is not None:
                queue.append((node.left, d+1))

            if node.right is not None:
                queue.append((node.right, d+1))

        return root

