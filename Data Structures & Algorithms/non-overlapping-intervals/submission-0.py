class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        cur_s, cur_e = intervals[0]
        ans = 0
        for i in intervals[1:]:
            s,e = i
            if  cur_e<=s:
                cur_s,cur_e = s,e
            else:
                ans +=1
                if e <= cur_e:
                    cur_s,cur_e = s,e
        return ans