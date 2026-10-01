class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
        for i in range(n-2,-1,-1):
            for j in range(n-1,i,-1):
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        for i in range(n):
            for j in range(i,n):
                if dp[i][j]:
                    ans+=1
        return ans
