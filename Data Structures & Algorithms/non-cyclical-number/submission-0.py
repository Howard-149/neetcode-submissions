class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            nxt = 0
            while n!= 0:
                nxt += (n%10)**2
                n = n//10
            n = nxt
        return True