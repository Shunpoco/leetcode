class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        
        res = [""] * len(words)
        for word in words:
            w = word[:len(word)-1]
            i = int(word[len(word)-1])
            
            res[i-1] = w
            
        return " ".join(res)
