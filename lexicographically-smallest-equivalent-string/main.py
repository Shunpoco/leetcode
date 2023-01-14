from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        memo = defaultdict(set)
        for c1, c2 in zip(s1, s2):
            memo[c1].add(c2)
            memo[c2].add(c1)

        fixed = [False] * 26
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if not fixed[ord(c)-ord('a')]:
                fixed[ord(c)-ord('a')] = True
                if memo.get(c) is None:
                    memo[c].add(c)

                else:
                    queue = memo[c]
                    while len(queue) > 0:
                        v = queue.pop()
                        if not fixed[ord(v)-ord('a')]:
                            cs = memo[v]
                            for cc in cs:
                                queue.add(cc)
                            memo[v] = set([c])
                            fixed[ord(v)-ord('a')] = True
                    memo[c] = set([c])

        r = ""
        for c in baseStr:
            r += list(memo[c])[0]

        return r
