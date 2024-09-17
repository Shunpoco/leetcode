class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        memo = defaultdict(int)

        for word in s1.split(" "):
            memo[word] += 1

        for word in s2.split(" "):
            memo[word] += 1

        result = []
        for k, v in memo.items():
            if v == 1:
                result.append(k)

        return result
