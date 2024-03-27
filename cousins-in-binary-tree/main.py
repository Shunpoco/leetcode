# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dx, dy = -1, -1

        q = [(root, 0)]

        while len(q) > 0:
            node, level = q.pop(0)

            if node.val == x:
                dx = level
            if node.val == y:
                dy = level

            if dx >= 0 and dx == dy:
                return True

            if node.left is not None and node.right is not None:
                if node.left.val == x and node.right.val == y or node.left.val == y and node.right.val == x:
                    return False

            if node.left is not None:
                q.append((node.left, level+1))
            if node.right is not None:
                q.append((node.right, level+1))

        return False

