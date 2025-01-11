class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        count = [0 for _ in range(26)]
        odd = 0
        for c in s:
            count[ord(c)-ord('a')] += 1

        for c in count:
            if c % 2 == 1:
                odd += 1

        return odd <= k

