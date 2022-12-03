from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        r = []
        for c, n in counter.most_common():
            r.append(c*n)
            
        return "".join(r)
