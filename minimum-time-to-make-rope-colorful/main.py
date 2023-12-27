class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cur = 0
        prev = -1
        result = 0
        while cur < len(colors):
            if prev >= 0 and colors[prev] == colors[cur]:
                if neededTime[prev] <= neededTime[cur]:
                    result += neededTime[prev]
                    prev = cur
                else:
                    result += neededTime[cur]
                                
            else:
                prev = cur
            
            cur += 1
            
        return result
