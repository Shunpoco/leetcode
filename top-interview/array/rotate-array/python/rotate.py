from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        Do not return anything, modify nums in-place instead.
        '''
        for _ in range(k):
            v = nums.pop(len(nums)-1)
            nums.insert(0, v)
