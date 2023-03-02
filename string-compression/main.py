from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        c = chars[0]
        l = 1

        for i in range(1, len(chars)):
            char = chars[i]

            if char == c:
                l += 1
            else:
                chars[idx] = c
                c = char
                idx += 1
                if l > 1:
                    if l < 10:
                        chars[idx] = str(l)
                        idx += 1
                    else:
                        t = l
                        digit = 0
                        while t > 0:
                            digit += 1
                            t //= 10
                        for i in range(digit-1, -1, -1):
                            chars[idx+i] = str(l%10)
                            l //= 10

                        idx += digit
                    l = 1

        chars[idx] = c
        idx += 1
        if l > 1:
            if l < 10:
                chars[idx] = str(l)
                idx += 1
            else:
                print(l, c)
                t = l
                digit = 0
                while t > 0:
                    digit += 1
                    t //= 10
                for i in range(digit-1, -1, -1):
                    chars[idx+i] = str(l%10)
                    l //= 10

                idx += digit


        return idx

