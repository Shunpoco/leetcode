class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pg, ps = 0, 0
        g.sort()
        s.sort()

        result = 0

        while pg < len(g) and ps < len(s):
            if g[pg] <= s[ps]:
                result += 1
                pg += 1
                ps += 1
            else:
                ps += 1

        return result
