class Solution:
    def countHomogenous(self, s: str) -> int:
        left, right = 0, 0

        mod = 10 ** 9 + 7
        result = 0
        while right < len(s):
            if s[left] == s[right]:
                right += 1
            else:
                result += (right - left + 1) * (right - left) // 2
                result %= mod
                left = right

        result += (right - left + 1) * (right - left) // 2
        result %= mod

        return result


