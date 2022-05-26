from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = self.binarySearch(num, dp)
            if i >= len(dp):
                dp.append(num)
            else:
                dp[i] = num
                
        return len(dp)
        
        
    def binarySearch(self, num: int, dp: List[int], start=0) -> int:
        l = len(dp)
        
        if l == 0:
            return start
        
        m = l//2
        
        v = dp[m]
        
        if v == num:
            return start+m
        elif v > num:
            return self.binarySearch(num, dp[:m], start)
        else:
            return self.binarySearch(num, dp[m+1:], start+m+1)
