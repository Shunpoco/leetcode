class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        freq = [0] * 3

        while right < len(s):
            freq[ord(s[right]) - ord("a")] += 1

            while self._has_all_chars(freq):
                result += len(s) - right

                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return result

    def _has_all_chars(self, freq: list) -> bool:
        return all(f > 0 for f in freq)
