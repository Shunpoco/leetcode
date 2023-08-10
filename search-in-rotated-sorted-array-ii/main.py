from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        rd = []
        memo = {}
        for num in nums:
            if memo.get(num) is None:
                rd.append(num)
                memo[num] = True

        n = len(rd)

        k = self.find(rd, 0, n-1)

        return self._search(rd, target, 0, n-1, k, n)


    def find(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left

        m = (left+right) // 2

        if nums[m] <= nums[right]:
            return self.find(nums, left, m)
        
        return self.find(nums, m+1, right)

    def _search(self, nums, target, left, right, k, n) -> bool:
        m = (left+right) // 2
        m_ = (m+k) % n
        print(left, right, m, m_, nums[m_])
        if left == right:
            return nums[m_] == target

        if nums[m_] == target:
            return True

        elif nums[m_] < target:
            return self._search(nums, target, m+1, right, k, n)
        
        return self._search(nums, target, left, m, k, n)

