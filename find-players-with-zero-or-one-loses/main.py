from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = [-1 for _ in range(100001)]
        losts = [0 for _ in range(100001)]
        
        for match in matches:
            if wins[match[0]] > 0:
                wins[match[0]] += 1
            else:
                wins[match[0]] = 1
                
            if wins[match[1]] == -1:
                wins[match[1]] = 0
                
            losts[match[1]] += 1
            
        
        ans0 = []
        ans1 = []
        
        for i in range(len(wins)):
            w = wins[i]
            l = losts[i]
            if w < 0:
                continue
            if l == 0:
                ans0.append(i)
                
            elif l == 1:
                ans1.append(i)
                
        return [ans0, ans1]

