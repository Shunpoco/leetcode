class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        cums = []
        t = 0

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                t += 1

            cums.append(t)

        result = []

        for query in queries:
            v = cums[query[1]]
            if query[0] != 0:
                v -= cums[query[0]-1]

            result.append(v)

        return result

