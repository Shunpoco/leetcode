class Solution:
    def countLargestGroup(self, n: int) -> int:
        memo = defaultdict(int)

        for v in range(1, n+1):
            s = self.calc(v)
            memo[s] += 1

        max_size = 1
        for size in memo.values():
            if max_size < size:
                max_size = size

        result = 0

        for size in memo.values():
            if max_size == size:
                result += 1

        return result

    def calc(self, n):
        result = 0

        while n > 0:
            result += n % 10
            n //= 10            

        return result

