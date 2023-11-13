import heapq

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        
        q = []

        for c in s:
            if c in vowels:
                heapq.heappush(q, c)

        result = []

        for i, c in enumerate(s):
            if c in vowels:
                result.append(heapq.heappop(q))
            else:
                result.append(c)

        return "".join(result)

