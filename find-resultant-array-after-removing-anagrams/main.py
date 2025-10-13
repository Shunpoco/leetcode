class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        encodes = []

        for word in words:
            t = [0 for _ in range(26)]
            for c in word:
                t[ord(c)-ord('a')] += 1

            r = ""
            for v in t:
                c = str(v)
                if len(c) == 1:
                    c = "0" + c

                r += c

            encodes.append(r)

        result = []
        for i in range(len(encodes)-1, 0, -1):
            if encodes[i] != encodes[i-1]:
                result.append(words[i])

        result.append(words[0])
        result.reverse()

        return result

