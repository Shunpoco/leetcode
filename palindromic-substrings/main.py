class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}

        result = 0

        for i in range(1, len(s)+1):
            for j in range(0, len(s)-i+1):
                if self.palindrome(s[j:j+i], memo):
                    result += 1

        return result

    def palindrome(self, s: str, memo) -> bool:
        if memo.get(s) is not None:
            return memo[s]

        if len(s) <= 1:
            return True

        result = False
        if s[0] == s[len(s)-1]:
            result |= self.palindrome(s[1:len(s)-1], memo)

        memo[s] = result

        return result
