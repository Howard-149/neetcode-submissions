class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            mask = 1 << i
            if mask&n:
                ans += 1
        return ans