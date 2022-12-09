# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = [(root, -1, -1)]
        result = -1

        while len(queue) > 0:
            node, minimum, maximum = queue.pop(0)
            if minimum == -1 and maximum == -1:
                minimum = node.val
                maximum = node.val
            else:
                result = max(abs(node.val-minimum), abs(node.val-maximum), result)
                if minimum > node.val:
                    minimum = node.val
                if maximum < node.val:
                    maximum = node.val
            if node.left is not None:
                queue.append((node.left, minimum, maximum))
            if node.right is not None:
                queue.append((node.right, minimum, maximum))

        return result
