class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = [s for s in palindrome]
        if len(palindrome) == 1:
            return ""
        
        odd = True if len(palindrome)%2 != 0 else False
        
        for i in range(len(palindrome)):
            if odd and i == len(palindrome)//2:
                continue
            
            if palindrome[i] != "a":
                palindrome[i] = "a"
                break
            
            else:
                if i == len(palindrome) - 1:
                    palindrome[i] = "b"
                    
                    
        return "".join(palindrome)
