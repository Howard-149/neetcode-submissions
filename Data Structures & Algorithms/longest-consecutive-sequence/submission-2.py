class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        ans = 0
        for n in nums:
            seen[n] = True
        for n in seen.keys():
            if seen.get(n-1,False):
                continue
            cnt = 1
            while seen.get(n+1,False):
                n+=1
                cnt+=1
            ans = max(cnt,ans)
        return ans