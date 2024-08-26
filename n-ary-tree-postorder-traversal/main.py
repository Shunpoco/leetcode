"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        self.calc(root, result)

        return result

    def calc(self, root, result):
        if root is None:
            return

        for c in root.children:
            self.calc(c, result)

        result.append(root.val)
