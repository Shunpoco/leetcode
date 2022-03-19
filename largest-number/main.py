class Largest(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = sorted(map(str, nums), key=Largest)
        
        l = ''.join(l)
        
        return "0" if l[0] == "0" else l
