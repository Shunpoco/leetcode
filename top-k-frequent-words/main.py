from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memory = defaultdict(int)
        for word in words:
            memory[word] -= 1
            
        hpq = []
        for key, val in memory.items():
            heapq.heappush(hpq, (val, key))
            
        result = heapq.nsmallest(k, hpq)
    
        return list(map(lambda x: x[1], result))
