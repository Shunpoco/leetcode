# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.result = []

        q = [(root, 0)]

        while len(q) > 0:
            v = q.pop(0)
            self.result.append(v[1])

            if v[0].left is not None:
                q.append((v[0].left, v[1]*2+1))

            if v[0].right is not None:
                q.append((v[0].right, v[1]*2+2))

    def find(self, target: int) -> bool:
        return target in self.result

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
