class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) 
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            cur_s = s[:i]
            for w in wordDict:
                m = len(w)
                if i>=m and cur_s[-m:] == w and not dp[i]:
                    dp[i] = dp[i-m]
        print(dp)
        return dp[-1]