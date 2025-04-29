class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)

        result = 0
        start = 0
        num_m = 0

        for end in range(len(nums)):
            if nums[end] == m:
                num_m += 1

            while num_m == k:
                if nums[start] == m:
                    num_m -= 1

                start += 1

            result += start

        return result

