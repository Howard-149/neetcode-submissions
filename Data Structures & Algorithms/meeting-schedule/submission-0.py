"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        cur_e = 0
        for i in intervals:
            s = i.start
            e = i.end
            if not cur_e <=s:
                return False
            cur_e = e
        return True