class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [0 for _ in range(len(prices))]

        for i in range(len(prices)):
            v = prices[i]

            t = i + 1

            while t < len(prices) and prices[t] > prices[i]:
                t += 1

            if t != len(prices):
                v -= prices[t]

            result[i] = v

        return result

