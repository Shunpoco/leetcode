class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta = [0] * (len(nums) + 1)

        for l, r in queries:
            delta[l] += 1
            delta[r+1] -= 1

        ops = []
        cur = 0
        for d in delta:
            cur += d
            ops.append(cur)

        for o, t in zip(ops, nums):
            if o < t:
                return False

        return True

