class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        increases = [1 for _ in range(n)]
        decreases = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    increases[i] = max(increases[i], increases[j]+1)

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    decreases[i] = max(decreases[i], decreases[j]+1)

        result = float("inf")

        for i in range(n):
            if increases[i] > 1 and decreases[i] > 1:
                result = min(result, n-increases[i]-decreases[i]+1)

        return result
