class Solution:
    def jump(self, nums: List[int]) -> int:
        result = [-1 for _ in range(len(nums))]
        result[len(nums)-1] = 0
        self.exec(0, nums, result)

        return result[0]

    def exec(self, idx: int, nums: List[int], result: List[int]):
        if result[idx] > -1:
            return

        r = 9999999999999999
        for i in range(1, nums[idx]+1):
            if idx + i < len(nums):
                self.exec(idx+i, nums, result)
                if result[idx+i] + 1 < r:
                    r = result[idx+i] + 1
        
        result[idx] = r

