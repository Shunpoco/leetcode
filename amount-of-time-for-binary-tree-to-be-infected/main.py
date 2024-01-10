# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        result = 0

        def DFS(node, start) -> int:
            if node == None:
                return 0

            leftD = DFS(node.left, start)
            rightD = DFS(node.right, start)

            if node.val == start:
                Solution.result = max(leftD, rightD)
                return -1

            elif leftD >= 0 and rightD >= 0:
                return max(leftD, rightD) + 1

            Solution.result = max(Solution.result, abs(leftD - rightD))

            return min(leftD, rightD) - 1

        DFS(root, start)

        return Solution.result
