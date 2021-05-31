from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = self._sort(nums)

        longest = 1
        temp = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                temp +=1
            elif nums[i+1] == nums[i]:
                continue            
            else:
                if temp > longest:
                    longest = temp
                temp = 1

        if temp > longest:
            longest = temp

        return longest

    
    def _sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = int(len(nums)/2)

        left = self._sort(nums[:m])
        right = self._sort(nums[m:])

        res = []

        while len(left) > 0 or len(right) > 0:
            if len(left) == 0:
                res.append(right.pop(0))

            elif len(right) == 0:
                res.append(left.pop(0))

            else:
                lc = left[0]
                rc = right[0]

                if lc < rc:
                    res.append(lc)
                    left.pop(0)
                else:
                    res.append(rc)
                    right.pop(0)


        return res

