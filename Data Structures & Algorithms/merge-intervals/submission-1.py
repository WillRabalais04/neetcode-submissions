class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals
            
        intervals = sorted(intervals, key = lambda x: x[0])
        idx = 0

        while idx < len(intervals):
            if idx + 1 >= len(intervals):
                break
            if intervals[idx][1] >= intervals[idx + 1][0]:
                intervals[idx][1] = max(intervals[idx][1], intervals[idx + 1][1])
                intervals.pop(idx + 1)
                continue
            idx += 1

        return intervals
        