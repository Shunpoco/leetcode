class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        m = len(nums) // 3
        result = []

        n = len(nums) // m
        t1 = 0
        t2 = n

        while t2 <= len(nums):
            arr = nums[t1:t2]
            if arr[-1] - arr[0] > k:
                return []

            result.append(arr)

            t1 = t2
            t2 += n

        return result

