class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            res.append(sum(list(
                map(
                    lambda x: self.abs(x, query) <= pow(query[2], 2),
                    points
                )
            )))
            
        return res
            
        
        
    def abs(self, x: List[int], b: List[int]) -> int:
        v1 = x[0] - b[0]
        v2 = x[1] - b[1]
                    
        return pow(v1, 2) + pow(v2, 2)
