from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        cur = self.root
        
        for char in word:
            cur = cur.nodes[char]
        cur.isEnd = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return cur.isEnd
    
    def startWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return True

    def noBranch(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.nodes:
                return False
            if len(cur.nodes) > 1:
                return False
            cur = cur.nodes[char]
        return True
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        minStr = strs[0]
        for s in strs:
            trie.insert(s)
            if len(s) < len(minStr):
                minStr = s
                
        for i in range(len(minStr)):
            s = minStr[0:len(minStr)-i]
            if trie.noBranch(s):
                return s
            
        return ''
