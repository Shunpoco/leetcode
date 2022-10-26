from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ht = {}
        
        s = 0
        for i, num in enumerate(nums):
            s += num
            c = s % k
            if c == 0 and i > 0:
                return True
            
            if ht.get(c) is not None:
                v = ht[c][0]
                if v+2 <= i:
                    return True
                ht[c].append(i)
                
            else:
                ht[c] = [i]

        # print(ht)
        return False
