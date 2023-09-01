from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]

        nex = 1
        for i in range(1, n+1):
            result.append(1+result[i-nex])
            if i == nex:
                nex *= 2

        return result
