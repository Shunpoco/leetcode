# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        level = 0
        left, right = 0, 0
        queue = [(root, 0, 1)]

        while len(queue) > 0:
            n, p, l = queue.pop(0)
            if l > level:
                if right - left + 1 > result:
                    result = right - left + 1

                level = l
                left, right = p, p

            if right < p:
                right = p

            if n.left is not None:
                queue.append((n.left, 2*p, l+1))
            if n.right is not None:
                queue.append((n.right, 2*p+1, l+1))

        if right - left + 1 > result:
            result = right - left + 1

        return result

