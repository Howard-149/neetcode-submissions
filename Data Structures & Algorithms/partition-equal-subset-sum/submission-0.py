class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        target = s/2
        cur = 0
        def BT(i,cur):
            if cur == target:
                return True
            if i >= len(nums):
                return False
            cur+=nums[i]
            if BT(i+1,cur):
                return True
            cur-=nums[i]
            if BT(i+1,cur):
                return True
            return False
        return BT(0,cur)
