class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None or (root.left is None and root.right is None):
            return

        left = root.left
        right = root.right

        root.left = None
        self.flatten(left)
        self.flatten(right)
        root.right = left

        next = root
        while next.right is not None:
            next = next.right

        next.right = right