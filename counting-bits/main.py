from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(0, n+1):
            if i == 0 or i == 1:
                result.append(i)
            else:
                if i % 2 == 0:
                    result.append(result[int(i/2)])
                else:
                    result.append(result[i-1]+1)
        return result
