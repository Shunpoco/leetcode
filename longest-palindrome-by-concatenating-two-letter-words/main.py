class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        memo = defaultdict(int)

        for i, word in enumerate(words):
            memo[word] += 1

        result = 0
        one = False

        for i, word in enumerate(words):
            if memo[word] == 0:
                continue

            memo[word] -= 1
            reverse = word[1]+word[0]
            if memo[reverse] > 0:
                memo[reverse] -= 1
                result += 4

            elif word == reverse and not one:
                one = True
                result += 2

        return result
