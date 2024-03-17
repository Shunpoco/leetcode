class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []

        idx = 0

        while idx < n and intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx += 1

        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1

        result.append(newInterval)

        while idx < n:
            result.append(intervals[idx])
            idx += 1

        return result
