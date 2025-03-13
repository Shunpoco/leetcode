class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total = 0
        k = 0

        arr = [0] * (n+1)

        for i in range(n):
            while total + arr[i] < nums[i]:
                k += 1

                if k > len(queries):
                    return -1

                l, r, v = queries[k-1]

                if r >= i:
                    arr[max(l, i)] += v
                    arr[r+1] -= v

            total += arr[i]

        return k
