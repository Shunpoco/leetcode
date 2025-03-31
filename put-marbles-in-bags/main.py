class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        pairs = [weights[i]+weights[i+1] for i in range(n-1)]
        pairs.sort()

        result = 0
        for i in range(k-1):
            result += pairs[n-2-i]-pairs[i]

        return result

