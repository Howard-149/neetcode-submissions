"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = [ i.start for i in intervals]
        e = [ i.end for i in intervals]
        s.sort()
        e.sort()
        i,j = 0,0
        cnt = 0
        ans = 0
        while i < len(s) and j < len(e):
            if s[i] < e[j]:
                cnt+=1
                i+=1
            else:
                cnt-=1
                j+=1
            ans = max(ans,cnt)
        return ans

