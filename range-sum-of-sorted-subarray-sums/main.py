class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        cums = [0]
        t = 0

        for num in nums:
            t += num
            cums.append(t)

        q = []
        for i in range(len(cums)):
            v = cums[i]
            for j in range(i+1, len(cums)):
                heapq.heappush(q, cums[j]-v)

        for _ in range(left-1):
            heapq.heappop(q)

        result = 0
        for _ in range(right-left+1):
            result += heapq.heappop(q)
            result %= 10 ** 9 + 7

        return result
