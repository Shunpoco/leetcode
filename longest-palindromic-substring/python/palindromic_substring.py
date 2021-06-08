class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        maxL = 1
        l = len(s)
        memory = {}
        for i in range(l):
            for j in range(l-1, i, -1):
                res, isPalindrome = self._isPalindrome(s, i, j, memory)
                if isPalindrome and len(res) > maxL:
                    result = res
                    maxL = len(res)
        return result


    def _isPalindrome(self, s: str, start: int, end: int, memory) -> bool:
        sub = s[start:end+1]
        tup = (start, end)
        if memory.get(tup) is not None:
            return sub, memory.get(tup)

        if start == end:
            memory[tup] = True
            return sub, True

        if end == start+1:
            isPalindrome = s[start] == s[end]
            memory[tup] = isPalindrome
            return sub, isPalindrome

        _, isPalindrome = self._isPalindrome(s, start+1, end-1, memory)

        isPalindrome = isPalindrome and s[start] == s[end]

        memory[tup] = isPalindrome

        return sub, isPalindrome
