class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        result = [[0, 0, 0] for _ in range(len(nums)//3)]
        idx = 0
        for i in range(len(nums)//3):
            if nums[idx+2] - nums[idx] <= k:
                result[i] = [nums[idx], nums[idx+1], nums[idx+2]]
                idx += 3
            else:
                return []

        return result

