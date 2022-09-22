class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        result = []
        for word in words:
            result.append(self.process(word))
            
        return " ".join(result)
    
    def process(self, word: str) -> str:
        l = len(word)
        r = ""
        for i in range(l-1, -1, -1):
            r += word[i]
            
        return r
