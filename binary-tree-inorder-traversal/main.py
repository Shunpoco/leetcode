
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if root:
            if root.left is not None:
                result.extend(self.inorderTraversal(root.left))

            result.append(root.val)

            if root.right is not None:
                result.extend(self.inorderTraversal(root.right))
            
        return result
