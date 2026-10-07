class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals
            
        intervals = sorted(intervals, key = lambda x: x[0])
        idx = 0
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
