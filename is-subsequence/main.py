from typing import Dict, Tuple

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        h = {}
        
        return self.check(s, t, h)
    
    def check(self, s: str, t: str, h: Dict[Tuple[str, str], bool]) -> bool:
        if len(s) == 0:
            h[(s, t)] = True
            return True
        
        if len(s) > len(t):
            h[(s, t)] = False
            return False
        
        if h.get((s, t)) is not None:
            return h.get((s, t))
        if s[0] == t[0]:
            result = self.check(s[1:], t[1:], h)
            h[(s, t)] = result
        else:
            result = self.check(s, t[1:], h)
            h[(s, t)] = result
            
        return result
