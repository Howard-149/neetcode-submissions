class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            if s[i-1] == "0" :
                if s[i-2] == "0" or ord(s[i-2]) - ord("0")>=3:
                    return 0
                dp[i] = dp[i-2]
            elif s[i-2] == "0" or (ord(s[i-2])-ord("0"))*10+ord(s[i-1]) -ord("0")>=27:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]