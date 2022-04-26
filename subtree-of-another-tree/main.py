# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        
        while len(stack) > 0:
            n1 = stack.pop()
            
            if n1.val == subRoot.val:
                # print(n1, subRoot)
                if check(n1, subRoot):
                    return True
                
            if n1.left:
                stack.append(n1.left)
            if n1.right:
                stack.append(n1.right)
                
        return False
    
def check(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
    stack = [(n1, n2)]
    
    while len(stack) > 0:
        t1, t2 = stack.pop()
        
        if t1 is None and t2 is None:
            continue
        
        if t1 and t2 is None or t1 is None and t2:
            return False
        if t1.val != t2.val:
            return False
        
        stack.append((t1.left, t2.left))
        stack.append((t1.right, t2.right))
        
    return True
