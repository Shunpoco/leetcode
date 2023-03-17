class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root

        for i, c in enumerate(word):
            end = True if i == len(word)-1 else False

            if cur.get(c) is None:
                cur[c] = [{}, end]
            else:
                cur[c][1] = True if end else cur[c][1]
            cur = cur[c][0]

    def search(self, word: str) -> bool:
        cur = self.root
        for i, c in enumerate(word):
            if cur.get(c) is None:
                return False
            if i == len(word)-1:
                return cur[c][1]
            cur = cur[c][0]

        return False            
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i, c in enumerate(prefix):
            if cur.get(c) is None:
                return False
            if i == len(prefix)-1:
                return True
            cur = cur[c][0]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
