class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        ans = float("-inf")
        for n in nums:
            s+=n
            ans = max(ans,s)
            if s<0:
                s = 0
        return ans