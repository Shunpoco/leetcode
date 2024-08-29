class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            
            if parent_x == parent_y:
                return
            
            if parent_x < parent_y:
                parent[parent_y] = parent_x
            else:
                parent[parent_x] = parent_y
                
            return
        
        def is_connected(stone1, stone2):
            if stone1[0] == stone2[0]:
                return True
            if stone1[1] == stone2[1]:
                return True
            return False
        
        for i, stone1 in enumerate(stones):
            for j, stone2 in enumerate(stones[i+1:], start=i+1):
                if is_connected(stone1, stone2):
                    union(i, j)
                    
        total_cnt = 0
        for i in range(len(parent)):
            if parent[i] != i:
                total_cnt += 1
                
        return total_cnt
