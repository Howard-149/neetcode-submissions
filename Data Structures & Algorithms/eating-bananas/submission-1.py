class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = (l+r)//2
            T = 0
            for p in piles:
                if p%mid != 0:
                    T+=p//mid+1
                else:
                    T+=p//mid
            if T <= h:
                ans = min(ans,mid)
                r = mid-1
            elif T > h:
                l = mid+1
        return ans