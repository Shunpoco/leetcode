class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word

        return ""

    def isPalindrome(self, word: str) -> bool:
        m = len(word) // 2

        for i in range(m):
            if word[i] != word[len(word)-1-i]:
                return False

        return True
