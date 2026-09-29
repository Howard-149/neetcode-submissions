class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates.sort()
        def BT(i,s):
            if s == target:
                ans.append(cur.copy())
                return
            elif s>target or i>=len(candidates):
                return
            cur.append(candidates[i])
            BT(i+1,s+candidates[i])
            cur.pop()
            while i<len(candidates)-1 and candidates[i+1] == candidates[i]:
                i+=1
            BT(i+1,s)
        BT(0,0)
        return ans