class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = []
        r_max = []
        M = 0
        for i in range(len(height)):
            l_max.append(M)
            M = max(M,height[i])
        M = 0
        for i in range(len(height)-1,-1,-1):
            r_max.append(M)
            M = max(M,height[i])
        r_max = r_max[::-1]
        ans = 0
        for i in range(len(height)):
            ans += max(min(l_max[i],r_max[i]) - height[i],0)
        return ans
