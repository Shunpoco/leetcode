# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = {}
        leafs = set()

        self.traverse(root, None, graph, leafs)

        result = 0

        for leaf in leafs:
            q = []
            seen = set()
            q.append(leaf)
            seen.add(leaf)

            for i in range(distance+1):
                l = len(q)
                for j in range(l):
                    curr = q.pop(0)
                    if curr in leafs and curr != leaf:
                        result += 1
                    if curr in graph:
                        for n in graph.get(curr):
                            if n not in seen:
                                q.append(n)
                                seen.add(n)

        return result // 2

    def traverse(self, curr, prev, graph, leafs):
        if curr is None:
            return

        if curr.left is None and curr.right is None:
            leafs.add(curr)

        if prev is not None:
            if prev not in graph:
                graph[prev] = []
            graph[prev].append(curr)
        
            if curr not in graph:
                graph[curr] = []
            graph[curr].append(prev)

        self.traverse(curr.left, curr, graph, leafs)
        self.traverse(curr.right, curr, graph, leafs)

    
