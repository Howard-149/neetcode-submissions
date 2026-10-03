class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        cur_s, cur_e = newInterval
        ans = []
        for i,(s,e) in enumerate(intervals):
            if cur_e <s:
                ans.append([cur_s,cur_e])
                for inter in intervals[i:]:
                    ans.append(inter)
                return ans
            elif cur_s<=s:
                cur_e = max(cur_e,e)
            elif cur_s>s and cur_s<=e:
                cur_s = s
                cur_e = max(cur_e,e)
            else:
                ans.append([s,e])
        ans.append([cur_s,cur_e])
        return ans 
                
                

                