class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = [0 for _ in range(101)]

        for num in nums:
            f[num] += 1

        m = max(f)

        r = 0
        for i, f_ in enumerate(f):
            if f_ == m:
                r += f_

        return r
