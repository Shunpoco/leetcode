class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        mem = [0]*26
        
        for c in sentence:
            mem[ord(c)-ord("a")] = 1

        return sum(mem) == 26
