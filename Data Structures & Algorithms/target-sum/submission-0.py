class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            next_dp = defaultdict(int)
            for cur_sum, cnt in dp.items():
                next_dp[cur_sum+n] += cnt
                next_dp[cur_sum-n] += cnt
            dp = next_dp
        return dp[target]


