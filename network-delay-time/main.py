class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        routes = []
        for i in range(n):
            t = []
            for time in times:
                if time[0]-1 == i:
                    t.append((time[2], time[1]-1))
            t.sort()
            routes.append(t)
            
        # print(routes)
        cost = [-1]*n
        cost[k-1] = 0
        
        dp(k-1, 0, routes, cost)
        
        if -1 in cost:
            return -1
        
        print(cost)
        
        return max(cost)
    

def dp(idx: int, cur: int, routes: List[List[int]], cost: List[int]):
    cands = routes[idx]
    # print(routes)
    
    for c in cands:
        if cost[c[1]] == -1 or cost[c[1]] > c[0] + cur:
            cost[c[1]] = c[0] + cur
            dp(c[1], c[0]+cur, routes, cost)
