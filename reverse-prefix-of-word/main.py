class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        p = ""
        i = 0
        while i < len(word):
            p = word[i] + p
            i += 1
            if word[i-1] == ch:
                return p + word[i:]

        return word
