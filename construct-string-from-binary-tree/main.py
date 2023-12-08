# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.sub(root)

    def sub(self, node) -> str:
        if node is None:
            return ""
        
        res = str(node.val)

        l = self.sub(node.left)
        r = self.sub(node.right)

        if l == "" and r != "":
            res += "()" + f"({r})"

        elif l != "" and r != "":
            res += f"({l})" + f"({r})"

        elif l != "" and r == "":
            res += f"({l})"

        return res
