class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        def getMax(nums):
            n = len(nums)
            dp = [0] * (n+1)
            dp[1] = nums[0]
            for i in range(2,n+1):
                dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
            return dp[-1]
        return max(getMax(nums[:-1]),getMax(nums[1:]))