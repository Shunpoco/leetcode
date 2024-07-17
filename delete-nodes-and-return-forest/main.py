# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []

        to_delete.sort()

        self.delete(root, None, to_delete, result)

        return result

    def delete(self, node, parent, to_delete, result):
        if node is None:
            return

        if node.val in to_delete:
            if parent is not None:
                if parent.left is not None and node == parent.left:
                    parent.left = None
                elif parent.right is not None and node == parent.right:
                    parent.right = None

            self.delete(node.left, None, to_delete, result)
            self.delete(node.right, None, to_delete, result)

        else:
            if parent is None:
                result.append(node)

            self.delete(node.left, node, to_delete, result)
            self.delete(node.right, node, to_delete, result)
