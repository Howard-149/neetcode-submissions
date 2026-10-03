class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        for i,n in enumerate(nums):
            if i > right:
                return False
            right = max(i+n,right)
        return right>=len(nums)-1