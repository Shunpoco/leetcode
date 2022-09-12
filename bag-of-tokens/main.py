class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        score = 0
        left = 0
        right = len(tokens) - 1
        
        while left <= right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
            else:
                if score > 0 and left != right:
                    power += tokens[right]
                    score -= 1
                    right -= 1
                else:
                    break
                    
        return score
