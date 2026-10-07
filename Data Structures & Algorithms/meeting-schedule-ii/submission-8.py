"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key = lambda x: x.start)
        
        room_end_times = []
        heapq.heappush(room_end_times, intervals[0].end)
        
       # iterate thru, freeing rooms if meeting ends before next starts
        for i in intervals[1:]:
            print(room_end_times)
            if room_end_times[0] <= i.start:
                heapq.heappop(room_end_times)
            heapq.heappush(room_end_times, i.end)
        return len(room_end_times)

        

        