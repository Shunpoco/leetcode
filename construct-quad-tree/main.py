from typing import List
"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        nodes = []
        for row in range(n):
            rows = []
            for col in range(n):
                rows.append(self.leaf(grid[row][col]))
            nodes.append(rows)

        while n > 1:
            t = []
            for row in range(n//2):
                r = []
                for col in range(n//2):
                    topLeft = nodes[0+row*2][0+col*2]
                    topRight = nodes[0+row*2][1+col*2]
                    bottomLeft = nodes[1+row*2][0+col*2]
                    bottomRight = nodes[1+row*2][1+col*2]

                    val = 0
                    isLeaf = 0
                    if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val:
                        val = topLeft.val
                        isLeaf = True
                    if isLeaf == 1:
                        node = self.leaf(val)
                    else:
                        node = Node(val, False, topLeft, topRight, bottomLeft, bottomRight)
                    
                    r.append(node)
                t.append(r)
            nodes = t
            n //= 2

        return nodes[0][0]


    def leaf(self, val: int) -> 'Node':
        return Node(val, True, None, None, None, None)
