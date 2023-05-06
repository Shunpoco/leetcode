from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        nums.sort()

        mod = 1000000007
        result = 0

        left, right = 0, n-1
        while left <= right:
            if nums[left]+nums[right] > target:
                right -= 1
            else:
                v = pow(2, right-left)
                result += v
                result %= mod
                left += 1

        return result



