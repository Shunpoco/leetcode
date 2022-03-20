class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        memory = {}
        for word in words:
            if memory.get(word):
                memory[word] += 1
            else:
                memory[word] = 1
            
        result = []
        for i in range(len(words[0])):
            result.extend(self.check(s, i, len(words), len(words[0]), memory))
                
        return result
    
    def check(self, s: str, start: int, num_words: int, len_word: int, memory: Dict) -> List[int]:
        m = memory.copy();
        
        l = start
        r = l + len_word
        result = []
        word_use = 0
        while r <= len(s):
            w = s[r-len_word:r]
            if m.get(w) is None:
                l = r
                word_use = 0
                m = memory.copy()
            else:
                while m.get(w) == 0:
                    m[s[l:l+len_word]] += 1
                    l += len_word
                    word_use -= 1
                word_use += 1
                m[w] -= 1
                
            if word_use == num_words:
                result.append(l)
            r += len_word
        print(result)
        return result
