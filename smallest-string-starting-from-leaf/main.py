# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        queue = [(root, "")]
        result = ""

        p = ord('a')
        while queue:
            node, val = queue.pop(0)

            val = chr(node.val + p) + val

            if node.left is None and node.right is None and (result == "" or result > val):
                result = val
                continue

            if node.left is not None:
                queue.append((node.left, val))

            if node.right is not None:
                queue.append((node.right, val))

        return result
 
