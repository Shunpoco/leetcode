from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.convert(pattern)
        converted = [self.convert(word) for word in words]
        result = []
        
        for word, c_word in zip(words, converted):
            if pattern == c_word:
                result.append(word)
                
        return result
        
        
    def convert(self, word: str) -> str:
        word = [c for c in word]
        mem = {}
        val = 0
        result = ""
        for c in word:
            if mem.get(c) is None:
                mem[c] = val
                val+= 1
            result += str(mem[c])
                
        return result
