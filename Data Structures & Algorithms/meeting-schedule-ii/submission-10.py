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

        unfreed_rooms = [] # store by end times
        heapq.heappush(unfreed_rooms, intervals[0].end)

        for i in intervals[1:]:
            print(unfreed_rooms)
            if unfreed_rooms[0] <= i.start:
                heapq.heappop(unfreed_rooms)
            heapq.heappush(unfreed_rooms, i.end)

        return len(unfreed_rooms)
        