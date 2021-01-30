class Solution:
  def isPalindrome(self, x: int)-> bool:
    if x < 0:
      return False


    palindrome = []

    while x > 0:
      palindrome.append(x % 10)
      x = x // 10
    

    l = len(palindrome)
    for i in range(l):
      if palindrome[i] != palindrome[l-1-i]:
        return False
    
    return True
