class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1

        while left < right and s[left] == s[right]:
            t = 0
            while left+t < right and s[left] == s[left+t]:
                t += 1
            u = 0
            while right-u > left and s[right] == s[right-u]:
                u += 1

            left += t
            right -= u


        return len(s[left:right+1])
