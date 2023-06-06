from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)

        arr.sort()
        diff = -1
        for i in range(n-1):
            v = arr[i+1] - arr[i]
            if diff >= 0 and diff != v:
                return False

            diff = v
        
        return True

