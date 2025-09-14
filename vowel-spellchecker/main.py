class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def de_vowel(word):
            return "".join("*" if c in 'aeiou' else c for c in word)

        words_set = set(wordlist)
        words_cap = {}
        words_vow = {}

        for w in wordlist:
            l = w.lower()
            words_cap.setdefault(l, w)
            words_vow.setdefault(de_vowel(l), w)

        def calc(query):
            if query in words_set:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryDe = de_vowel(queryL)
            if queryDe in words_vow:
                return words_vow[queryDe]

            return ""

        return list(map(calc, queries))

