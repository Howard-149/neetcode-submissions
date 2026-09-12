class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        for i in range(N-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = N-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    ans.append((nums[i],nums[j],nums[k]))
                    j+=1
                    while j<N and nums[j] == nums[j-1]:
                        j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                    while k>j and nums[k] == nums[k+1]:
                        k-=1
                else:
                    j+=1
                    while j<N and nums[j] == nums[j-1]:
                        j+=1
        return ans
