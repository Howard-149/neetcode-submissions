class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def BT(i):
            if i>= len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            BT(i+1)
            subset.pop()
            BT(i+1)
        BT(0)
        return ans