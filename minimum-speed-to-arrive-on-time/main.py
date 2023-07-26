from typing import List

import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        if hour <= n-1:
            return -1

        return self.search(1, 10000000, dist, hour)

        
    def search(self, left: int, right: int, dist: List[int], hour: float) -> int:
        m = (left+right) // 2

        h = self.calc(dist, m)
        if h > hour:
            if left == right:
                return -1
            return self.search(m+1, right, dist, hour)

        if left == right:
            return m

        v = self.search(left, m, dist, hour)
        if v != -1:
            return v
        return m

        
    def calc(self, dist: List[int], speed: int) -> float:
        r = 0.0

        for i, d in enumerate(dist):
            r += d/speed
            if i < len(dist)-1:
                r = math.ceil(r)

        return r

