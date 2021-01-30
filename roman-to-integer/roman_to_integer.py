class Solution:
  def romanToInt(self, s: str)-> int:
    matcher = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    }

    ints = []
    for i in range(len(s)):
      ints.append(matcher[s[i]])

    lenInts = len(ints)
    result = 0
    i = 0
    while i < lenInts:
      temp = ints[i]
      if i < lenInts - 1 and temp < ints[i+1]:
        temp = ints[i+1] - temp
        i = i + 1
      result = result + temp
      i = i + 1    
    
    return result

