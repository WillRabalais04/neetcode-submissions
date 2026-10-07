"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = list(map(lambda x : (x.start, 's'), intervals))
        end = list(map(lambda x: (x.end, 'e'), intervals))
        schedule = start + end
        schedule.sort()
        schedule = list(map(lambda x: x[1] , schedule))

        free = []
        
        
        mcm = 0 # max concurrent meetings
        cm = 0 # concurrent meetings

        for c in schedule:
            if c == 's':
                cm += 1
            elif c == 'e':
                cm -= 1
            mcm = max(mcm, cm)

        # print(f"start: {start}")
        # print(f"end: {end}")
        return mcm


       