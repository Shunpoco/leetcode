# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = [(root, root.val, root.val)]
        result = 0

        while len(queue) > 0:
            node, minimum, maximum = queue.pop(0)

            for t in [node.left, node.right]:
                if t is not None:
                    diff = max(abs(t.val - minimum), abs(t.val- maximum))
                    if diff > result:
                        result = diff

                    queue.append((t, min(t.val, minimum), max(t.val, maximum)))

        return result
