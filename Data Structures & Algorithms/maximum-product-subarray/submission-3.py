class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for n in nums[1:]:
            tmp = cur_max
            cur_max = max(n*tmp,n*cur_min,n)
            cur_min = min(n*tmp,n*cur_min,n)
            ans = max(ans,cur_max)
        return ans
            