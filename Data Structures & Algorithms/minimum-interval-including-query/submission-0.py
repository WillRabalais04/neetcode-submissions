class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        
        ret = {}
        mh = []
        i = 0
        n = len(intervals)
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        for q_val, q_idx in sorted_queries:
            # add all intervals that start before or at current query
            while i < n and intervals[i][0] <= q_val:
                start, end = intervals[i][0], intervals[i][1]
                length = end - start + 1
                heapq.heappush(mh, (length, end))
                i += 1
            # remove all intervals that end before current query
            while mh and mh[0][1] < q_val:
                heapq.heappop(mh)

            # store range 
            if mh:
                ret[q_idx] = mh[0][0]
            else:
                ret[q_idx] = -1

        return [ret[i] for i in range(len(queries))]