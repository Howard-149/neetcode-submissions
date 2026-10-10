class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        ans = 0
        maxf = 0
        cnt = defaultdict(int)
        while r < len(s):
            cnt[s[r]] += 1
            maxf = max(maxf,cnt[s[r]])
            while r-l+1 - maxf >k:
                cnt[s[l]] -= 1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans