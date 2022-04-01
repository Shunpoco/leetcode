# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = [root, None]
        first = True
        while len(queue) > 0:
            v = queue.pop(0)
            if v is None:
                first = True
                while len(queue) > 0 and queue[0] is None:
                    queue.pop(0)
                if len(queue) > 0:
                    queue.append(None)
            else:
                if first:
                    result.append(v.val)
                    first = False
                if v.right:
                    queue.append(v.right)
                if v.left:
                    queue.append(v.left)

        return result
