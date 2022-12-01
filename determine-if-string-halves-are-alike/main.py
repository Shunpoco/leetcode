class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        l = len(s)
        
        c1 = 0
        for i in range(0, l//2):
            if s[i] in vowels:
                c1 +=1
                
        c2 = 0
        for i in range(l//2, l):
            if s[i] in vowels:
                c2 += 1
                
        return c1 == c2
