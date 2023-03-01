from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.exec(nums)

    def exec(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = len(nums) // 2
        n1 = self.exec(nums[:m])
        n2 = self.exec(nums[m:])

        r = []
        while len(n1) > 0 and len(n2) > 0:
            if n1[0] < n2[0]:
                r.append(n1.pop(0))
            else:
                r.append(n2.pop(0))

        if len(n1) > 0:
            r.extend(n1)
        elif len(n2) > 0:
            r.extend(n2)

        return r

