from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        s = [c for c in s]
        
        chars = defaultdict(list)

        for i, c in enumerate(s):
            chars[c].append(i)

        result = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if len(chars[c]) <= 1:
                continue

            t = chars[c]

            left, right = t[0], t[-1]

            result += len(set(s[left+1:right]))

        return result
