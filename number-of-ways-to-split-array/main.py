class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cums = []
        t = 0
        for num in nums:
            t += num
            cums.append(t)

        result = 0

        for i in range(len(nums)-1):
            l, r = cums[i], cums[-1] - cums[i]

            if l >= r:
                result += 1

        return result

