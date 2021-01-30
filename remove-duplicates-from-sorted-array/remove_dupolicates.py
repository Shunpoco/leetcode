from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    while i < len(nums):
      if nums[i] == nums[i-1]:
        nums.pop(i)
        continue
      i += 1
      
    return len(nums)

# see https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/984561/Python-beats-98
