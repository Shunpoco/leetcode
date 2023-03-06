from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for num in arr:
            diff = num - prev - 1
            if diff > 0:
                if diff >= k:
                    break
                k -= diff
        
            prev = num

        return prev + k
