# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        memory = defaultdict(int)
        
        stack = [root]
        
        while len(stack) > 0:
            node = stack.pop();
            
            memory[node.val] += 1
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        
        maximum = 0
        result = []
        for k,v in memory.items():
            if v == maximum:
                result.append(k)
                maximum = v
            elif v > maximum:
                result = [k]
                maximum = v
                
        return result
