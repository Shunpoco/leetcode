class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []

        for i in range(n):
            if len(stack) == 0 or nums[stack[-1]] > nums[i]:
                stack.append(i)

        mw = 0

        for j in range(n-1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] <= nums[j]:
                mw = max(mw, j - stack[-1])
                stack.pop()

        return mw
