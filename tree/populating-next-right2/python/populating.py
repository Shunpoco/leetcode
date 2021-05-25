from typing import List


class Node:
    def __init__(self, val:int=0, left:'Node'=None, right:'Node'=None, next:'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root:'Node') -> 'Node':
        if root is None or (root.left is None and root.right is None):
            return root
        
        nodes = [root]

        self._connect(nodes)
        return root

    def _connect(self, nodes:List['Node']):
        if len(nodes) == 0:
            return

        newNodes = []
        right = None

        while len(nodes) > 0:
            left = nodes.pop(0)
            if left is not None:
                left.next = right
                newNodes.append(left.right)
                newNodes.append(left.left)
                right = left

        self._connect(newNodes)

