class Solution:
    def minOperations(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        for num in nums:
            memo[num] += 1

        result = 0
        for _, v in memo.items():
            t = v // 3
            while t >= 0:
                c = v - 3 * t
                if c % 2 == 0:
                    result += t
                    result += c // 2
                    break
                t -= 1

            if t == -1:
                return -1

        return result
