class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = []

        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))

        result = 0

        while len(pq) > 0:
            v = heapq.heappop(pq)
            if nums[v[1]] == -1:
                continue

            result += nums[v[1]]
            nums[v[1]] = -1
            if v[1] < len(nums)-1:
                nums[v[1]+1] = -1
            if v[1] > 0:
                nums[v[1]-1] = -1

        return result

