from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        result = []
        
        l = []
        l[:0] = target
        target = l
        
        start = ["?"]*len(target)
        
        idx = 0
        while target != start and idx <= len(target) - len(stamp):
            v = target[idx:idx+len(stamp)]
            
            if self.equal(stamp, v):
                target[idx:idx+len(stamp)] = "?"*len(stamp)
                result.append(idx)
                idx = 0
            else:
                idx += 1
                
        if target != start:
            return []
        
        return list(reversed(result))


    def equal(self, stamp: str, s: str) -> bool:
        if len(stamp) != len(s) or s == ["?"]*len(stamp):
            return False
        
        for c1, c2 in zip(stamp, s):
            if c1 != c2 and c2 != "?":
                return False
            
        return True
