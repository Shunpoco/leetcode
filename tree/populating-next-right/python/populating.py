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

        stack = []

        stack.append(root.right)
        stack.append(root.left)

        self._set(stack)

        return root


    def _set(self, stack: List['Node']):
        if None in stack:
            return
        c = None
        s = []
        while len(stack) > 0:
            n = stack.pop(0)
            s.append(n.right)
            s.append(n.left)
            n.next = c
            c = n

        self._set(s)
