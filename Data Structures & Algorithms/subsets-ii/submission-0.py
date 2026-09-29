class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []
        def BT(i):
            if i>=len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            BT(i+1)
            cur.pop()
            while i<len(nums)-1 and nums[i+1] == nums[i]:
                i+=1
            BT(i+1)
        BT(0)
        return ans