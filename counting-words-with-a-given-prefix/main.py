class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(list(map(lambda x: 1 if len(x) >= len(pref) and x[:len(pref)] == pref else 0, words)))

