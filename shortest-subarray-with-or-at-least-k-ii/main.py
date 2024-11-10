class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        mins = float("inf")

        start, end = 0, 0
        bits = [0 for _ in range(32)]

        while end < len(nums):
            self.update(bits, nums[end], 1)
            while start <= end and self.convert(bits) >= k:
                mins = min(mins, end-start+1)
                self.update(bits, nums[start], -1)
                start += 1

            end += 1

        return -1 if mins == float("inf") else mins

    def convert(self, bits):
        result = 0
        for p in range(32):
            if bits[p]:
                result |= 1 << p

        return result

    def update(self, bits, num, diff):
        for p in range(32):
            if num & (1<<p):
                bits[p] += diff
