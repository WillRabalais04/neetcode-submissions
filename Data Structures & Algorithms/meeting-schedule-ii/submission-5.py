"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = [(i.start, 1) for i in intervals] + [(i.end, -1) for i in intervals]
        events.sort()
        
        mcm = 0 # max concurrent meetings
        cm = 0 # concurrent meetings

        for _, change in events:
            cm += change
            mcm = max(mcm, cm)
            
        return mcm


       