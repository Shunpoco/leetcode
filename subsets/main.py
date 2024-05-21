class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = []
        for i in range(2**n):
            t = []
            for j in range(n):
                if j > i:
                    break
                if (2 ** j) & i > 0:
                    t.append(nums[j])

            result.append(t)

        return result

