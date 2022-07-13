import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if root is None:
            return result
        
        q = queue.Queue()
        q.put((root, 0))
        
        while q.empty() == False:
            v = q.get()
            if len(result) == v[1]:
                result.append([v[0].val])
            else:
                result[v[1]].append(v[0].val)
                
            if v[0].left:
                q.put((v[0].left, v[1]+1))
            if v[0].right:
                q.put((v[0].right, v[1]+1))
                
        return result
