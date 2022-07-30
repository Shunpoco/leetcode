from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:        
        mem = defaultdict(lambda: 0)
        count = 0
        for word in words2:
            t = defaultdict(lambda: 0)
            for c in word:
                t[c] += 1
                
            for k, v in t.items():
                if mem[k] < v:
                    count -= mem[k]
                    count += v
                    mem[k] = v
            
        result = []
        for word1 in words1:
            counter = count
            d = mem.copy()
            
            for c in word1:
                if d[c] > 0:
                    d[c] -= 1
                    counter -= 1
                            
            if counter == 0:
                result.append(word1)
            
        return result
