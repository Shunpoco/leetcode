from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        visited = [False for _ in range(len(bank))]
        
        def search(s: str) -> int:
            if s == end:
                return 0
            
            candidates = []
            for i, b in enumerate(bank):
                if not visited[i] and self.distance(s, b) == 1:
                    candidates.append((i, b))
                    
            if len(candidates) == 0:
                return -1
            
            r = -1
            for i, b in candidates:
                visited[i] = True
                t = 1+search(b)
                if t > 0 and (r == -1 or r > t):
                    r = t
                    
                visited[i] = False
                
            return r
        
        return search(start)
        
    def distance(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        
        r = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                r += 1
                
        return r
