# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        queue = [(root.left, 0, True), (root.right, 0, False)]

        while len(queue) > 0:
            node, v, is_left = queue.pop(0)
            if node is None:
                if v > result:
                    result = v
                continue
            else:
                v += 1
                if v > result:
                    result = v
                if is_left:
                    queue.append((node.right, v, False))
                    queue.append((node.left, 0, True))
                else:
                    queue.append((node.left, v, True))
                    queue.append((node.right, 0, False))

        return result



