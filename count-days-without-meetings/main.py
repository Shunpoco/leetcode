class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        result = 0

        meetings.sort()

        cur = 1
        for i, m in enumerate(meetings):
            if i == 0:
                result += max(0, m[0]-cur)
            else:
                result += max(0, m[0]-cur-1)
            cur = max(cur, m[1])

        result += max(0, days-cur)

        return result

        
