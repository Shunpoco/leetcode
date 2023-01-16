class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = self._insert(intervals, newInterval)
        print(intervals)
        return self.merge(intervals)
    
    
    
    def _insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if len(intervals) == 1:
            if intervals[0] < newInterval:
                return [intervals[0], newInterval]
            else:
                return [newInterval, intervals[0]]
            
        m = int(len(intervals)/2)
        
        l = intervals[:m]
        r = intervals[m:]
        
        if intervals[m] > newInterval:
            l = self._insert(l, newInterval)
        else:
            r = self._insert(r, newInterval)
            
        l.extend(r)
        
        return l
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals are already sorted
        
        res = [intervals.pop(0)]
        i = 0
        
        while intervals:
            s = res[i]
            l = intervals.pop(0)
            if s[1] >= l[0]:
                # overlapping
                res[i] = [s[0], max(s[1], l[1])]
                
            else:
                res.append(l)
                i += 1
                
        return res
