class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        max_len = len(word) - numFriends + 1

        result = ""

        for i in range(len(word)):
            c = word[i:i+max_len]

            if c > result:
                result = c

        return result

