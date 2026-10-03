class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        right = 0
        prev_right = 0
        for i,n in enumerate(nums):
            if right>=len(nums)-1:
                return jumps
            if i > prev_right:
                jumps+=1
                prev_right = right
            if i + nums[i]>right:
                right = i+nums[i]
                if right>=len(nums)-1:
                    jumps+=1
                    return jumps
        return jumps
               