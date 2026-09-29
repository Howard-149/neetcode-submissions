class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def BT(i,s):
            if s == target:
                ans.append(cur.copy())
                return
            elif s > target:
                return
            if i>=len(nums):
                return
            cur.append(nums[i])
            s += nums[i]
            BT(i,s)
            cur.pop()
            s-=nums[i]
            BT(i+1,s)
        BT(0,0)
        return ans