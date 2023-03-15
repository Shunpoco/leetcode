from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [(root, 1)]
        f = False
        l = 0
        c = 0
        while len(q) > 0:
            node, level = q.pop(0)
            if level > l:
                if c > 0 and c != pow(2, level-2):
                    print(node.val, level, c)
                    return False
                l = level
                f = False
                c = 0

            c += 1
            if f:
                if node.left is not None or node.right is not None:
                    return False

            else:
                if node.left:
                    q.append((node.left, level+1))
                else:
                    f = True
                if node.right:
                    if f:
                        return False
                    q.append((node.right, level+1))
                else:
                    f = True

        return True
                        
