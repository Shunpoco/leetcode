from typing import List, Dict

class WordDictionary:

    def __init__(self):
        self.root =  [{}, False]

    def addWord(self, word: str) -> None:
        cur = self.root[0]
        end = False
        for i, c in enumerate(word):
            if i == len(word)-1:
                end = True
            if cur.get(c) is None:
                cur[c] = [{}, end]
            else:
                cur[c][1] |= end
            cur = cur[c][0]


    def search(self, word: str) -> bool:
        def exec(l, w) -> bool:
            if len(w) == 0:
                return l[1]

            if w[0] != '.':
                if l[0].get(w[0]) is None:
                    return False
                return exec(l[0][w[0]], w[1:])
                
            else:
                candidates = list(l[0].keys())
                v = False
                for c in candidates:
                    v |= exec(l[0][c], w[1:])
                    if v:
                        return v
            return False

        return exec(self.root, word)
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
