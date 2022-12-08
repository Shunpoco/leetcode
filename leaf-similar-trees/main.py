# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        v1 = self.getSequence(root1)
        v2 = self.getSequence(root2)

        return v1 == v2

    def getSequence(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []

        while len(stack) > 0:
            node = stack.pop(-1)
            if node.left is None and node.right is None:
                result.append(node.val)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return result
