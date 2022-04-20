"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        
        memory = {}
        stack = [(node, None)]
        
        while len(stack) > 0:
            n, prev = stack.pop()
            if memory.get(n.val):
                v = memory[n.val]
            else:
                v = Node(n.val)
                memory[n.val] = v
            if prev:
                if v in prev.neighbors:
                    continue
                prev.neighbors.append(v)
            
            print(n.val)
            for i in n.neighbors:
                print(i.val)
                stack.append((i, v))
                
        return memory[node.val]
