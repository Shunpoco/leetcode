from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        se = set([x for x in range(1, n+1)])
        r = []
        s = 1
        d = 1
        r.append(s)
        for i in range(-1 * k, 0):
            n = s - d * i
            r.append(n)
            s = n
            d = d * -1
        r.extend(se.difference(set(r)))   
        return r

