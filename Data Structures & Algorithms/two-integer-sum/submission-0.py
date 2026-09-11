class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if seen.get(target-n,None) is not None:
                return [seen[target-n],i]
            seen[n] = i