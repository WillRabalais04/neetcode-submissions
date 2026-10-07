class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        if n == 0:
            return [newInterval]

        l,r = 0, n - 1
        idx = n
        while l <= r:
            m = (l + r) // 2
            if intervals[m][1] >= newInterval[0]:
                idx = m
                r = m - 1
            else:
                l = m + 1
       
        res = intervals[:idx]
       
        i = idx
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            print(newInterval)
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        res.extend(intervals[i:])
        return res

       