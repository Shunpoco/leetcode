# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queueo = [(original, 1, "left")]
        queuec = [(cloned, 1, "left")]
        
        while len(queueo) > 0:
            no, lo, po = queueo.pop(0)
            nc, lc, pc = queuec.pop(0)
            
            if no == target:
                if lo == lc and po == pc:
                    return nc
                
            if no.left:
                queueo.append((no.left, lo+1, "left"))
                queuec.append((nc.left, lc+1, "left"))

            if no.right:
                queueo.append((no.right, lo+1, "right"))
                queuec.append((nc.right, lc+1, "right"))
                
        return cloned
