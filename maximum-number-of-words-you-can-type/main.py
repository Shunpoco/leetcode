class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")

        broken_memo = {}
        for c in brokenLetters:
            broken_memo[c] = True

        result = len(words)

        for word in words:
            for c in word:
                if broken_memo.get(c):
                    result -= 1
                    break

        return result

