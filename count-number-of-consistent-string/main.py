class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        memo = defaultdict(bool)

        for c in allowed:
            memo[c] = True

        result = len(words)

        for word in words:
            for c in word:
                if not memo[c]:
                    result -= 1
                    break

        return result