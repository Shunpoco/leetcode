class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        hq = []
        delta = [0] * (len(nums) + 1)
        ops = 0

        j = 0
        for i, num in enumerate(nums):
            ops += delta[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(hq, -queries[j][1])
                j += 1

            while ops < num and len(hq) > 0 and -hq[0] >= i:
                ops += 1
                delta[-heappop(hq)+1] -= 1

            if ops < num:
                return -1

        return len(hq)

