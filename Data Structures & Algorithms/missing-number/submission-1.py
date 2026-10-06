class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor = xor^n
        ref = 0
        for i in range(len(nums)+1):
            ref ^=i
        return ref^xor