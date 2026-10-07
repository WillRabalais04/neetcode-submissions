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
        
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0].end)
        
       
        for i in intervals[1:]:
            print(free_rooms)
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i.end)
        return len(free_rooms)

        

        