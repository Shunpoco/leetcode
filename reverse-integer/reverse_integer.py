class Solution:
  def reverse(self, x: int)->int:
    x_str = str(x)
    res = ''
    if x_str[0] == '-':
      res += x_str[0]
      x_str = x_str[1:]

    zero_flg = True
    for i in range(len(x_str)):
      if x_str[-(i+1)] == 0 and zero_flg:
        continue
      zero_flg = False
      res += x_str[-(i+1)]

    result = int(res)

    if result > 2**31 - 1 or result < -2**31:
      result = 0
    return result


  def reverseAnother(self, x: int)->int:
    # https://leetcode.com/problems/reverse-integer/discuss/980189/reverse-integer-Simple-Python-solution
    output = 0
    digit = 1

    if x < 0:
      digit = -1
      x *= -1

    while x:
      output = output * 10 + x%10
      x = x // 10

    output *= digit

    if output > 2**31-1 or output < -2**31:
      output = 0

    return output
