class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cur_max = 1
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[j]< nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
                    if dp[i] > cur_max:
                        cur_max = dp[i]
                        break
                elif nums[j] == nums[i]:
                    dp[i] = max(dp[i],dp[j])
                    break
        return cur_max
