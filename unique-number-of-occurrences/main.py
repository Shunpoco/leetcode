from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = [0 for _ in range(1001)]
        
        mem = defaultdict(int)
        for num in arr:
            mem[num] += 1
            
        for _, v in mem.items():
            if counter[v] > 0:
                return False
            counter[v] += 1
            
        return True
