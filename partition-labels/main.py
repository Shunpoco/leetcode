class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = [0 for _ in range(26)]
        for i, c in enumerate(s):
            letters[ord(c)-ord('a')] = i

        start = 0
        end = 0
        sizes = []

        for i, c in enumerate(s):
            end = max(end, letters[ord(c)-ord('a')])

            if i == end:
                sizes.append(i-start+1)
                start = i + 1

        return sizes
