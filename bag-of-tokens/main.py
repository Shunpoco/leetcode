class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        r = 0

        tokens.sort()
        left, right = 0, len(tokens)-1

        while left <= right:
            if tokens[left] <= power:
                r += 1
                power -= tokens[left]
                left += 1
            else:
                if left == right or r == 0:
                    break
                r -= 1
                power += tokens[right]
                right -= 1

        return r
