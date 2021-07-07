class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self._count(root, 0)

    def _count(self, root: TreeNode, count: int) -> int:
        if root is None:
            return count

        count += 1

        return max(self._count(root.left, count), self._count(root.right, count))


# Using stack (Depth first search)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        md = 0
        if root is None:
            return md
        
        stack = []
        
        stack.append((root, 1))
        
        while stack:
            node, level = stack.pop(-1)
            
            if node is None:
                continue
            
            if node.left is None and node.right is None:
                if level > md:
                    md = level
                continue
                
            stack.append((node.left, level+1))
            stack.append((node.right, level+1))
            
        return md