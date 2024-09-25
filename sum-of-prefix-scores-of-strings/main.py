class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        memo = defaultdict(int)

        for word in words:
            for i in range(1, len(word)+1):
                memo[word[:i]] += 1

        result = []
        for word in words:
            t = 0
            for i in range(1, len(word)+1):
                t += memo[word[:i]]

            result.append(t)

        return result
