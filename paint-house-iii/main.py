from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.memo = [
            [
                [-1 for _ in range(21)] for _ in range(100)
            ] for _ in range(100)
        ]
        
        self.MAX_COST = 1000001
        
        answer = self.findMinCost(houses, cost, target, 0, 0, 0)
        
        if answer == self.MAX_COST:
            return -1
        else:
            return answer
        
    def findMinCost(self, houses: List[int], cost: List[List[int]], targetCount: int, currIdx: int, neighborhoodCount: int, prevHouseColor: int) -> int:
        if (currIdx == len(houses)):
            if neighborhoodCount == targetCount:
                return 0
            else:
                return self.MAX_COST
            
        if (neighborhoodCount > targetCount):
            return self.MAX_COST
        
        if (self.memo[currIdx][neighborhoodCount][prevHouseColor] != -1):
            return self.memo[currIdx][neighborhoodCount][prevHouseColor]
        
        minCost = self.MAX_COST
        
        if houses[currIdx] != 0:
            newNeighborhoodCount = neighborhoodCount
            if houses[currIdx] != prevHouseColor:
                newNeighborhoodCount += 1
            minCost = self.findMinCost(houses, cost, targetCount, currIdx+1, newNeighborhoodCount, houses[currIdx])
            
        else:
            totalColors = len(cost[0])
            
            for color in range(1, totalColors+1):
                newNeighborhoodCount = neighborhoodCount
                if color != prevHouseColor:
                    newNeighborhoodCount += 1
                    
                currCost = cost[currIdx][color-1] + self.findMinCost(houses, cost, targetCount, currIdx+1, newNeighborhoodCount, color)
                
                if currCost < minCost:
                    minCost = currCost
                    
        self.memo[currIdx][neighborhoodCount][prevHouseColor] = minCost
        
        return minCost

