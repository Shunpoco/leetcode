class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = {}
        r, _ = self.calc(s, wordDict, d)

        if len(r) == 1 and r[0] == "":
            return []

        return r

    
    def calc(self, word, dic, d) -> (List[str], bool):
        if len(word) == 0:
            return [""], True

        if d.get(word) is not None:
            return d[word]

        r = []
        for w in dic:
            n = len(w)
            if len(word) >= n and word[:n] == w:
                t = w
                v, b = self.calc(word[n:], dic, d)
                if b:
                    for v_ in v:
                        if v_ != "":
                            r.append(t + " " + v_)
                        else:
                            r.append(t)

        if len(r) == 0:
            d[word] = ([""], False)
            return [""], False

        return r, True
