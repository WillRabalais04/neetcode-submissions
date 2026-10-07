class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])

        i = 0
        n = len(intervals)
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                continue
            merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

        