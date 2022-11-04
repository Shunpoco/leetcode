class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [c for c in s]
        vowels = []
        position = []
        for i, c in enumerate(s):
            if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(c)
                position.append(i)
                
        position.reverse()
        
        for p, c in zip(position, vowels):
            s[p] = c
            
        return ''.join(s)
