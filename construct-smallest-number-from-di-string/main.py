class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.result = []

        self.calc(0, 0, pattern)

        return "".join(self.result[::-1])

    def calc(self, cur, count, pattern):
        if cur != len(pattern):
            if pattern[cur] == "I":
                self.calc(cur+1, cur+1, pattern)

            else:
                count = self.calc(cur+1, count, pattern)

        self.result.append(str(count+1))

        return count + 1

