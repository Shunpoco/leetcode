class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.end = False
        self.children = []
        
    def addChild(self, child: 'TrieNode'):
        self.children.append(child)

        
    def searchChild(self, char: str) -> 'TrieNode':
        for child in self.children:
            if child.val == char:
                return child
            
        return None
    
    
    def makeEnd(self):
        self.end = True
        

    def isEnd(self) -> bool:
        return self.end
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        
        for i in range(len(word)):
            char = word[i]
            child = cur.searchChild(char)
            if child is not None and i == len(word)-1:
                child.makeEnd()
            if child is None:
                child = TrieNode(char)
                if i == len(word)-1:
                    child.makeEnd()
                cur.addChild(child)
            cur = child
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        
        for i in range(len(word)):
            char = word[i]
            child = cur.searchChild(char)
            if child is None:
                return False
            
            if i == len(word)-1 and child.isEnd():
                return True
            
            cur = child

        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            child = cur.searchChild(char)
            if child is None:
                return False
            
            if i == len(prefix)-1:
                return True
            cur = child
            
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Imlementation in https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58953/AC-Python-solution-using-defaultdict

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        curr = self.root

        for char in word:
            curr = curr.nodes[char]

        curr.isWord = True


    def search(self, word):
        curr = self.root

        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]

        return curr.isWord


    def startsWith(self, prefix):
        curr = self.root

        for char in prefix:
            if char not in curr.nodes:
                return False

            curr = curr.nodes[char]

        return True
