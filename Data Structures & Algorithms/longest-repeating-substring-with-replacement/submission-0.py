class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        r = 0
        maxf = 0
        ans = 0
        while r < len(s):
            c = s[r]
            cnt[c]+=1
            maxf = max(maxf,cnt[c])
            while r-l+1 - maxf>k:
                cnt[s[l]] -=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
            
            