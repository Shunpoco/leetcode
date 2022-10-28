from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = defaultdict(list)
        
        for s in strs:
            v = "".join(sorted(s))
            memory[v].append(s)
            
        r = []
        for _, v in memory.items():
            r.append(v)
            
        return r
