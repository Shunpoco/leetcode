class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            c = 0
            for j in range(len(goal)):
                if s[(j+i)%len(s)] != goal[j]:
                    break
                c += 1

            if c == len(s):
                return True

        return False
