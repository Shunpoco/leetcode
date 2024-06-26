# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def marr(node):
            if node is None:
                return

            arr.append(node.val)

            marr(node.left)
            marr(node.right)

        marr(root)

        arr.sort()

        def mtree(arr):
            if len(arr) == 0:
                return None

            m = len(arr) // 2

            node = TreeNode(arr[m])
            node.left = mtree(arr[:m])
            node.right = mtree(arr[m+1:])

            return node

        return mtree(arr)
