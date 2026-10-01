class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        ans = s[0]
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
        for i in range(n-2,-1,-1):
            for j in range(n-1,i,-1):
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j]:
                    if j-i+1 > max_len:
                        ans = s[i:j+1]
                        max_len = max(max_len,j-i+1)
        return ans

                