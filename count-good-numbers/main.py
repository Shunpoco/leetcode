class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def calc(x: int, y: int) -> int:
            result, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    result = result * mul % MOD
                mul = mul * mul % MOD

                y //= 2

            return result

        return calc(5, (n+1)//2) * calc(4, n//2) % MOD

