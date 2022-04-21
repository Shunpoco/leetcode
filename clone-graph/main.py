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

        memory = {node.val: Node(node.val)}
        
        stack = [node]
        
        while len(stack) > 0:
            n = stack.pop()
            
            v = memory[n.val]
            
            for i in n.neighbors:
                if memory.get(i.val):
                    v_ = memory[i.val]
                    v.neighbors.append(v_)
                else:
                    v_ = Node(i.val)
                    v.neighbors.append(v_)
                    memory[i.val] = v_
                    stack.append(i)
                

        return memory[node.val]
