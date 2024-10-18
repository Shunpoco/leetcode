class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = 0
        for num in nums:
            m |= num

        dp = {}

        result = 0
        for i in range(len(nums)):
            self.calc(i, 0, nums, m, dp)
            result += dp[(i, 0)]

        return result

    def calc(self, idx, cur, nums, target, dp):
        if dp.get((idx, cur)) is not None:
            return

        t = cur
        cur |= nums[idx]

        if cur == target:
            dp[(idx, t)] = pow(2, len(nums)-1-idx)
            return

        
        r = 0
        for i in range(idx+1, len(nums)):
            self.calc(i, cur, nums, target, dp)

            r += dp[(i, cur)]

        dp[(idx, t)] = r

        return
