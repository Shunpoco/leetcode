from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        if self.isLeaf(root):
            if targetSum == root.val:
                return [[root.val]]
            return []
        
        v = targetSum - root.val
        
        result = []
        
        if root.left is not None:
            r = self.pathSum(root.left, v)
            if len(r) > 0:
                for res in r:
                    t = [root.val]
                    t.extend(res)
                    result.append(t)
        
        if root.right is not None:
            r = self.pathSum(root.right, v)
            if len(r) > 0:
                for res in r:
                    t = [root.val]
                    t.extend(res)
                    result.append(t)
                    
        return result
                
        
    def isLeaf(self, root: TreeNode):
        if root.left is None and root.right is None:
            return True
        return False
        