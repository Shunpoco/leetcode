from typing import List

lass Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        idx = 0
        t = []
        l = 0
        for idx in range(len(words)):
            v = words[idx]
            lv = len(v) if l == 0 else len(v)+1
            if l + lv <= maxWidth:
                t.append(v)
                l += lv
            else:
                # process
                diff = maxWidth - l
                if len(t) > 1:
                    spaces = [" " * (1 + diff // (len(t) - 1)) for _ in range(len(t)-1)]
                    spaces.append("")
                else:
                    spaces = [" " * diff]
                diff -= len("".join(spaces)) - (len(t) - 1)
                print(diff, len(spaces), spaces, t)
                for i in range(diff):
                    spaces[i] += " "
                r = ""
                for a, b in zip(t, spaces):
                    r += a + b

                result.append(r)
                t = [v]
                l = len(v)

        spaces = []
        if len(t) > 1:
            spaces = [" " for _ in range(len(t)-1)]

        spaces.append(" " * (maxWidth - l))

        r = ""
        for a, b in zip(t, spaces):
            r += a + b

        result.append(r)


        return result

