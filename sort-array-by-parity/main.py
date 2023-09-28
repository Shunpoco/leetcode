from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if num % 2 == 0:
                t = [num]
                t.extend(result)
                result = t
            else:
                result.append(num)

        return result

