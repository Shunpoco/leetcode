class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        m = max(nums)

        arr = [0 for _ in range(m + len(nums) + 2)]

        for num in nums:
            arr[num] += 1

        r = 0
        for i in range(len(arr)-1):
            if arr[i] > 1:
                r += arr[i] - 1
                arr[i+1] += arr[i] - 1

        return r

