class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.calc(word, k) - self.calc(word, k+1)

    def calc(self, word, k):
        result = 0

        start = 0
        end = 0

        vc = {}
        cc = 0

        while end < len(word):
            v = word[end]

            if v in self.vowels:
                vc[v] = vc.get(v, 0) + 1

            else:
                cc += 1

            while len(vc) == 5 and cc >= k:
                result += len(word) - end
                s = word[start]
                if s in self.vowels:
                    vc[s] = vc.get(s) - 1

                    if vc[s] == 0:
                        vc.pop(s)

                else:
                    cc -= 1
                start += 1

            end += 1

        return result

