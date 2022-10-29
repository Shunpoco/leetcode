from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = list(zip(plantTime, growTime))
        
        times.sort(key=lambda x: -x[1])
        
        ret, cur = 0, 0
        
        for plant, grow in times:
            cur += plant
            ret = max(ret, cur+grow)
            
        return ret
