class Solution:
    def lengthOfLastWord(self, s: str)-> int:
        c = s
        # prepare
        while len(c) > 0:
            if c[-1] == ' ':
                c = c[:len(c)-1]
            else:
                break
        a = c.split(' ')
        return len(a[-1])
