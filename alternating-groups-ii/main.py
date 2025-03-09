class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = len(colors)
        result = 0

        c = 1
        last = colors[0]

        for i in range(1, l+k-1):
            idx = i % l

            if colors[idx] == last:
                c = 1
                last = colors[idx]
                continue

            c += 1

            if c >= k:
                result += 1

            last = colors[idx]

        return result

