class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split(" ")

        for i, word in enumerate(l):
            if len(word) < len(searchWord):
                continue
            if word[:len(searchWord)] == searchWord:
                return i + 1

        return -1
