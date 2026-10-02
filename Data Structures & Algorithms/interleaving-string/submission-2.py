class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a = len(s1)
        b = len(s2)
        if a+b != len(s3):
            return False
        if not a or not b:
            return s3 == s1 or s3 == s2
        dp = [[False] * (b+1) for _ in range(a+1)]
        dp[0][0] = True
        for i in range(a+1):
            for j in range(b+1):
                if not dp[i][j]:
                    dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        return dp[a][b]