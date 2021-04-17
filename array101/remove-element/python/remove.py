from typing import List

class Solution:
    def removeElement(self, nums:List[int], val:int)->int:
        l = len(nums)
        i = 0
        c = 0
        r = 0
        while c < l:
            v = nums[i]
            if v == val:
                nums[i:l-1] = nums[i+1:]
                nums[l-1] = v
                r += 1
            else:
                i += 1
            c += 1

        return l - r
