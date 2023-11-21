class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        memo = defaultdict(list)

        for i, num in enumerate(nums):
            rev = self.rev(num)

            memo[num-rev].append(i)

        result = 0
        for _, v in memo.items():
            result += len(v) * (len(v)-1) // 2

            result %= 10 ** 9 + 7

        return result

    def rev(self, num: int) -> int:
        r = 0
        while num > 0:
            r *= 10
            r += num%10
            num = num // 10

        return r

# a + rev(b) = rev(a) + b = X
# X -a = rev(b)
# X - rev(a) = b
# a - rev(a) = b - rev(b)
