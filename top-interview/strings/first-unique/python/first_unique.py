class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}

        for i in range(len(s)):
            if h.get(s[i]) is None:
                h[s[i]] = {'ar': [i], 'c': 1}
                continue
            h[s[i]]['ar'].append(i)
            h[s[i]]['c'] += 1

        res = []
        for k in h.keys():
            n = h[k]
            if n['c'] > 1:
                continue
            res.extend(n['ar'])

        if len(res) == 0:
            return -1

        return min(res)
