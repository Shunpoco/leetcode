class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        cur = ""
        count = 0
        for c in word:
            if c == cur:
                count += 1

                if count == 9:
                    comp += "9" + cur
                    cur = ""
                    count = 0

            elif cur == "":
                cur = c
                count = 1

            else:
                comp += str(count) + cur
                cur = c
                count = 1

        if count > 0:
            comp += str(count) + cur

        return comp                                        
