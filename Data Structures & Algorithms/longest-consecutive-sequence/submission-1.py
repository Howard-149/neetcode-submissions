class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        ans = 0
        for n in nums:
            seen[n] = seen.get(n,0)+1
        for k in seen.keys():
            if seen.get(k-1,0):
                continue
            else:
                l=1
                while seen.get(k+l,0):
                    l+=1
                ans = max(ans,l)
        return ans