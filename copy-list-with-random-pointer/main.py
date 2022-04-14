"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c = []
        o = []
        r = []
        
        cur = head
        while cur:
            v = Node(cur.val, None, None)
            if cur.random:
                if cur.random in o:
                    i = o.index(cur.random)
                    v.random = c[i]
                else:
                    r.append((len(c), cur.random))      
            
            if len(c) > 0:
                c[-1].next = v
            c.append(v)
            o.append(cur)
            
            cur = cur.next

        while len(r) > 0:
            i, v = r.pop()
            j = o.index(v)
            c[i].random = c[j]

        if len(c) > 0:
            return c[0]
        else:
            return None
