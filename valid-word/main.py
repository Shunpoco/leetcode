class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        ascii_num_lower = ord('0')
        ascii_num_upper = ord('9')
        ascii_uppercase_lower = ord('A')
        ascii_uppercase_upper = ord('Z')
        ascii_lowercase_lower = ord('a')
        ascii_lowercase_upper = ord('z')

        vowels = [ord(x) for x in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']]

        has_vowel = False
        has_consonant = False

        for c in word:
            v = ord(c)
            if v >= ascii_num_lower and v <= ascii_num_upper:
                continue
            elif v >= ascii_uppercase_lower and v <= ascii_uppercase_upper:
                if v in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif v >= ascii_lowercase_lower and v <= ascii_lowercase_upper:
                if v in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            else:
                return False

        return has_vowel and has_consonant

