# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        memo = {}

        for d in descriptions:
            if memo.get(d[0]) is None:
                p = TreeNode(val=d[0])
            else:
                p = memo[d[0]][0]

            if memo.get(d[1]) is None:
                c = TreeNode(val=d[1])
            else:
                c = memo[d[1]][0]

            if d[2] == 1:
                p.left = c
            else:
                p.right = c

            memo[d[1]] = [c, p]

            if memo.get(d[0]) is not None:
                memo[d[0]] = [p, memo[d[0]][1]]
            else:
                memo[d[0]] = [p, None]

        for _, v in memo.items():
            if v[1] is None:
                return v[0]
        
        return None
