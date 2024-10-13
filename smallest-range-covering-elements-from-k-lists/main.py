class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        q = []
        maxv = float("-inf")
        s = 0
        e = float("inf")

        for i in range(len(nums)):
            heapq.heappush(q, (nums[i][0], i, 0))
            maxv = max(maxv, nums[i][0])

        while len(q) == len(nums):
            minv, row, col = heapq.heappop(q)

            if maxv - minv < e - s:
                s = minv
                e = maxv

            if col + 1 < len(nums[row]):
                nextv = nums[row][col+1]
                heapq.heappush(q, (nextv, row, col+1))
                maxv = max(maxv, nextv)

        return [s, e]
