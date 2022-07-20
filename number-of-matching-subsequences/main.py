from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)
            
            
        for c in s:
            candidates = word_dict[c]
            word_dict[c] = []
            
            for candidate in candidates:
                if len(candidate) == 1:
                    count += 1
                    
                else:
                    word_dict[candidate[1]].append(candidate[1:])
                    
        return count
