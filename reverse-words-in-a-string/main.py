class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        r = ""
        print(l)
        ll = []
        for l_ in l:
            if l_ != "":
                ll.append(l_)
                
        for i in range(len(ll)):
            v = ll[len(ll)-1-i]
            if i != 0:
                r += " "
            r += v

        return r
