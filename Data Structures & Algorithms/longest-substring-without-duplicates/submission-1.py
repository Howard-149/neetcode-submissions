class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        L = 0
        R = L
        ans = 0
        while R < len(s):
            r = s[R]
            while seen[r]:
                seen[s[L]] -= 1
                L += 1
            seen[r] += 1
            ans = max(ans, R - L + 1)
            R += 1
        return ans
