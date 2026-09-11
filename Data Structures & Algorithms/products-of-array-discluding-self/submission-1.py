class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        P = 1
        S = 1
        for n in nums[:-1]:
            P*=n
            prefix.append(P)
        for n in nums[:0:-1]:
            S*=n
            suffix.append(S)
        suffix = suffix[::-1]
        ans = [prefix[i]*suffix[i] for i in range(len(nums)) ]
        return ans


            
