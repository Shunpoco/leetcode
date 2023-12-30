from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        memo = defaultdict(int)

        for word in words:
            for c in word:
                memo[c] += 1

        n = len(words)
        for _, count in memo.items():
            if count % n != 0:
                return False

        return True
