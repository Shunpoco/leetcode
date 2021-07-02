class Solution:
    def isPalindrome(self, s: str) -> bool:
        filetered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercases = map(lambda ch: ch.lower(), filetered_chars)
        
        filtered_list = list(lowercases)
        reversed_list = filtered_list[::-1]
        
        return filtered_list == reversed_list
