class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >=nums[l] and nums[mid] <= nums[r]:
                return nums[l]
            elif nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] <= nums[l]:
                r = mid
        