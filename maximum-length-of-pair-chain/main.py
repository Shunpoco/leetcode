from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])

        result = 1
        prev = pairs[0]

        for i in range(1, len(pairs)):
            if prev[1] < pairs[i][0]:
                result += 1
                prev = pairs[i]

        return result
