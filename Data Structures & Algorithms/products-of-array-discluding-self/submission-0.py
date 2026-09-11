class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt+=1
                continue
            p*=n
        if zero_cnt>1:
            return [ 0 for i in nums]
        elif zero_cnt == 1:
            return [ p if i == 0 else 0 for i in nums ]
        else:
            return [ p//i for i in nums]