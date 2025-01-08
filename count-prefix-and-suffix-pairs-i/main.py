class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0

        for i in range(len(words)):
            str1 = words[i]
            for j in range(i+1, len(words)):
                str2 = words[j]

                if self.isPrefixAndSuffix(str1, str2):
                    result += 1

        return result


    def isPrefixAndSuffix(self, str1, str2) -> bool:
        if len(str1) > len(str2):
            return False

        return str1 == str2[:len(str1)] and str1 == str2[len(str2)-len(str1):]
