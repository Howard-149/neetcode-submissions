class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * 3 # buy, sell, cooldown
        dp[0] = -prices[0]
        for i in range(1,len(prices)):
            tmp_0 = dp[0]
            tmp_1 = dp[1]
            dp[0] = max(dp[0], dp[2]-prices[i])
            dp[1] = tmp_0+prices[i]
            dp[2] = max(tmp_1,dp[2])
        return max(dp[0],dp[1],dp[2])