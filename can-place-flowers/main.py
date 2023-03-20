from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        l = [0]
        l.extend(flowerbed)
        for i in range(1, len(l)-1):
            if n == 0:
                break
            if l[i-1] + l[i] + l[i+1] == 0:
                l[i] = 1
                n -= 1
        
        return n == 0


