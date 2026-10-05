class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        cur_s, cur_e = intervals[0]
        ans = []
        for i in intervals[1:]:
            s,e = i
            if not cur_e<s:
                cur_s = min(cur_s,s)
                cur_e = max(cur_e,e)
            else:
                ans.append([cur_s,cur_e])
                cur_s,cur_e = s,e
        ans.append([cur_s,cur_e])
        return ans